from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
