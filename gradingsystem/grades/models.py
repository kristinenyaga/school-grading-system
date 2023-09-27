from django.db import models
from django.core.exceptions import ValidationError
from students.models import Student
from terms.models import Term
def validate_value(value):
   if value > 100:
        raise ValidationError('Value must be less than or equal to 100')

# Create your models here.
class Grade(models.Model):
  gradeId = models.IntegerField(primary_key=True)
  examType= models.CharField(max_length=55)
  maths= models.PositiveIntegerField()
  english= models.PositiveIntegerField()
  kiswahili= models.PositiveIntegerField()
  physics= models.PositiveIntegerField()
  biology= models.PositiveIntegerField()
  chemistry= models.PositiveIntegerField()
  history= models.PositiveIntegerField()
  geography= models.PositiveIntegerField()
  cre= models.PositiveIntegerField()
  studentadmno = models.ForeignKey(Student, on_delete=models.CASCADE)
  termId=models.ForeignKey(Term, on_delete=models.CASCADE)

  class Meta:
    ordering = ['gradeId']
  def __str__(self) -> str:
     return self.studentadmno
