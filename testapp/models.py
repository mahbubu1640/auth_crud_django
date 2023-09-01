from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=10, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)
    file = models.FileField(upload_to='employee_files/', blank=True, null=True)

    def __str__(self):
        return self.name
