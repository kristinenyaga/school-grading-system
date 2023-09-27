from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=255, null=False)
    telephone = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.teacher_name

