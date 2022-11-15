from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return self.first_name
