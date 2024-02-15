from django.db import models

class employee(models.Model):
    emp_id = models.CharField(max_length = 7)
    emp_name = models.CharField(max_length = 30)
    emp_age = models.IntegerField(default = 21)
    emp_email = models.EmailField()
    emp_gender = models.CharField(max_length = 1)
    emp_salary = models.IntegerField()

