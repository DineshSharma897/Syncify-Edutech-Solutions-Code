from django.db.models import Avg, F, FloatField, ExpressionWrapper
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

from .models import Student, Test
from .serializers import StudentSerializer, TestSerializer

# Create your views here.
AVG_PERCENT = Avg(
    ExpressionWrapper(
        (F('tests__score') * 100.0) / F("tests__max_score"),
        output_field=FloatField()
    )
)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'], url_path='performance')
    def performance(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'details': 'Student not found'}, status=404)
        
        qs = Test.objects.filter(student=student)
        agg = qs.aggregate(average_score=Avg(
            ExpressionWrapper(
                (F('score') * 100.0) / F('max_score'),
                output_field=FloatField()
            )
        ))
        latest = qs.first()

        resp = {
            'student': student.name,
            'average_score': round(agg['average_score'] or 0.0, 2),
            'latest_test': None
        }
        if latest:
            resp['latest_test'] = {
                'student': latest.subject,
                'score': latest.score,
                'date': latest.date.isoformat(),
            }
        return Response(resp, status=200)
    
    @action(detail=False, methods=['get'], url_path='top-performers')
    def top_performance(self, request):
        try:
            limit = int(request.query_params.get('limit', 3))
            if limit <=0:
                limit = 3
        except ValueError:
            limit = 3

        students = (
            Student.objects
            .filter(test__isnull=False)
            .annotate(avg_pct= AVG_PERCENT)
            .order_by('-avg_pct')[:limit]
        )

        data = [
            {'student': s.name, 'average_score': round((s.avg_pct or 0.0), 2)}
            for s in students
        ]
        return Response(data, status=200)
    
    # @action(detail=False, methods=['get'], url_path='top-performers-sql')
    # def top_performance_sql(self, request):
    #     try:
    #         limit = int(request.query_params.get('limit', 3))
    #     except ValueError:
    #         limit = 3

    #     query = """
    #         SELECT s.id, s.name,
    #                 Round(AVG((t.score * 100.0) / t.max_score), 2) AS avg_pct
    #         FROM api_student s
    #         JOIN api_test t ON s.id = t.student_id
    #         GROUP BY s.id, s.name
    #         ORDER BY avg_pct DESC
    #         LIMIT %s;
    #     """

    #     with connection.cursor() as cursor:
    #         cursor.execute(query, [limit])
    #         rows = cursor.fetchall()
        
    #     data = [
    #         {"student": rows[1], "averahe_score": rows[2]} for row in rows
    #     ]

    #     return Response(data, status=200)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.select_related('student').all()
    serializer_class = TestSerializer