from django.db import models
from django.core.validators import MinValueValidator
from classes.models import Class

# Create your models here.


class Student(models.Model):
    studentadmno = models.IntegerField(
        validators=[MinValueValidator(1000)],
        primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    slug = models.SlugField()
    guardian_telephone = models.CharField(max_length=255, null=False)
    guardian_email = models.CharField(max_length=255, null=False)
    guardian_name = models.CharField(max_length=255, null=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        ordering = ['studentadmno']

    def __str__(self) -> str:
        return self.first_name
