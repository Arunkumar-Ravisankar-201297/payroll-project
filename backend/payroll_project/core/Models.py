from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('company', 'Company'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
