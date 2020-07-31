from django.db import models
# Create your models here.



class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_id = models.CharField(max_length=30)
    emp_Email= models.CharField(max_length=30)
    
    
    
