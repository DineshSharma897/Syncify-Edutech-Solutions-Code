from rest_framework import generics, views, response, status
from django.db.models import Avg, F, FloatField
from .models import Student, Test
from .serializers import StudentSerializer, TestSerializer


class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TestCreate(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class StudentPerformance(views.APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return response.Response({"error": "Not found"}, status=404)

        avg_score = (
            Test.objects.filter(student=student)
            .annotate(pct=F("score") * 100.0 / F("max_score"))
            .aggregate(avg=Avg("pct"))
        )["avg"]

        latest = (
            Test.objects.filter(student=student).order_by("-date").values().first()
        )

        return response.Response({
            "student": student.name,
            "average_score": round(avg_score or 0, 2),
            "latest_test": latest
        })


class TopPerformers(views.APIView):
    def get(self, request):
        limit = int(request.GET.get("limit", 3))
        qs = (
            Student.objects
            .annotate(avg=Avg(F("tests__score") * 100.0 / F("tests__max_score"), output_field=FloatField()))
            .order_by("-avg")[:limit]
        )
        data = [{"student": s.name, "average_score": round(s.avg or 0, 2)} for s in qs]
        return response.Response(data)
