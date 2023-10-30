from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    """Contact object"""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    user = models.ForeignKey(User, related_name="contacts", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)