from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    promoted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
