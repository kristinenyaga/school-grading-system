from django.db import models
from django.core.exceptions import ValidationError

def validate_value(value):
   if value > 100:
        raise ValidationError('Value must be less than or equal to 100')

# Create your models here.
class Grades(models.Model):
  gradeId = models.IntegerField(primary_key=True)
  examType= models.CharField(max_length=55)
  maths= models.PositiveIntegerField(validators=[validate_value])
  english= models.PositiveIntegerField(validators=[validate_value])
  kiswahili= models.PositiveIntegerField(validators=[validate_value])
  physics= models.PositiveIntegerField(validators=[validate_value])
  biology= models.PositiveIntegerField(validators=[validate_value])
  chemistry= models.PositiveIntegerField(validators=[validate_value])
  history= models.PositiveIntegerField(validators=[validate_value])
  geography= models.PositiveIntegerField(validators=[validate_value])
  cre= models.PositiveIntegerField(validators=[validate_value])

  class Meta:
    ordering = ['gradeId']
  def __str__(self) -> str:
     return self.grades
