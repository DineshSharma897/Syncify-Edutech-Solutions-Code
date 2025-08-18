from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name} ({self.department})"
    
class Test(models.Model):
    student =models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tests')
    subject = models.CharField(max_length=120)
    score = models.IntegerField()
    max_score = models.IntegerField()
    date = models.DateField()

    class Meta:
        ordering = ['-date', '-id']