from django.db import models


# Create your models here.
class Language(models.Model):
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(default="doe@example.com")
    password = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
