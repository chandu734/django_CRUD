from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    salary = models.FloatField( )
    designation = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"
    

    

