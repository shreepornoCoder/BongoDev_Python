from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="student_name", max_length=250)
    stu_class = models.IntegerField(verbose_name="student_class")