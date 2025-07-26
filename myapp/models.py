from django.db import models

# Create your models here.


class HOME(models.Model):
    heading=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/home')
