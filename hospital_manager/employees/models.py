from django.db import models
from departments.models import Departments
from department_heads.models import Departmentheads

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_no = models.IntegerField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='Employ')
    description = models.CharField(max_length=100)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    report_to = models.ForeignKey(Departmentheads,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
