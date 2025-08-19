from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="tests")
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    max_score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}"
