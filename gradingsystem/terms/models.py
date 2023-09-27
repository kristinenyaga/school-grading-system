from django.db import models

# Create your models here.
class Term(models.Model):
  termId = models.IntegerField(primary_key=True)
  termName = models.CharField(max_length=55)
  termStart = models.DateField()
  termEnd = models.DateField()
  class Meta:
    ordering = ['termId']
  def __str__(self) -> str:
      return self.termName
     