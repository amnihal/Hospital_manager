from django.db import models
from departments.models import Departments

# Create your models here.
class Departmentheads(models.Model):
    dhead_name = models.CharField(max_length=100)
    emp_no = models.IntegerField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='Departmentheads')
    description = models.CharField(max_length=100)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.dhead_name

  
    
