from django.db import models
from teachers.models import Teacher

# Create your models here.


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    year_joined = models.CharField(max_length=255)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['year_joined']

    def __str__(self) -> str:
        return self.year_joined