from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ['name', 'email']
