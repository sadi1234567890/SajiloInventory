from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length= 200, null=True)
    phone = models.CharField(max_length=20, null=True)
    joined_date = models.DateField(null=True, blank=True)
    total_leaves = models.IntegerField(default=0)
    attendance = models.IntegerField(default=0)
    department = models.CharField(max_length=100, null=True, blank=True)
 

    def __str__(self):
        return f'{self.staff.username}-Profile'