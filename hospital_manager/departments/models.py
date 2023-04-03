from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Departments')
    description = models.TextField()
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name