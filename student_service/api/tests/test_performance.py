# from django.test import TestCase
# from api.models import Student, Test
# from datetime import date

# class PerformanceAPITest(TestCase):
#     def setUp(self):
#         self.s = Student.objects.create(name='Alice', email='alice@x.com', department='CSE')
#         Test.objects.create(student=self.s, subject='Math', score=80, max_score=100, date=date(2025,8,1))
#         Test.objects.create(student=self.s, subject='Physics', score=90, max_score=100, date=date(2025,8,10))

#     def test_performance(self):
#         url = f"/api/students/{self.s.id}/performance/"
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(resp.json()['student'], 'Alice')
#         self.assertEqual('average_score', resp.json())
#         self.assertEqual('latest_test', resp.json())