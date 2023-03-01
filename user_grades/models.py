from django.db import models

# Create your models here.
class UserGrade(models.Model):
    name = models.CharField(max_length=20, default='newbie')
    def __str__(self):
        return self.name