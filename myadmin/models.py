from django.db import models

# Create your models here.


class ABOUT1(models.Model):
    heading=models.CharField(max_length=200)
    caption1=models.CharField(max_length=200)
    caption2=models.CharField(max_length=200)
    caption3=models.CharField(max_length=200)
    image=models.ImageField(upload_to="static/about")

class CONTACT1(models.Model):
    image=models.ImageField(upload_to='static/conatact')
    caption1=models.CharField(max_length=200)
    caption2=models.CharField(max_length=200)
    cpation3=models.CharField(max_length=200)
    caption4=models.CharField(max_length=200)





class CONTACT_INFO(models.Model):
    image=models.ImageField(upload_to='static/conatact')
    heading=models.CharField(max_length=200)
    caption1=models.CharField(max_length=200)
    caption2=models.CharField(max_length=200)
    cpation3=models.CharField(max_length=200)



class REGISTRATION(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    



class CONTACT(models.Model):
    name=models.CharField(max_length=200)
    people=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    message=models.CharField(max_length=400)


class PIZZA(models.Model):
    heading=models.CharField(max_length=200)
    caption=models.CharField(max_length=200)
    range=models.CharField(max_length=200)

class SALADS(models.Model):
    heading=models.CharField(max_length=200)
    caption=models.CharField(max_length=200)
    range=models.CharField(max_length=200)

class STARTER(models.Model):
    heading=models.CharField(max_length=200)
    caption=models.CharField(max_length=200)
    range=models.CharField(max_length=200)
    
class DAY(models.Model):
    sunday=models.CharField(max_length=200)
    monday=models.CharField(max_length=200)
    tuesday=models.CharField(max_length=200)
    wednesday=models.CharField(max_length=200)
    thurday=models.CharField(max_length=200)    
    friday=models.CharField(max_length=200)
    saturday=models.CharField(max_length=200)



class DAY1(models.Model):
    sunday2=models.CharField(max_length=200)
    sunday1=models.CharField(max_length=200)
    monday1=models.CharField(max_length=200)
    monday2=models.CharField(max_length=200)
    tuesday1=models.CharField(max_length=200)
    tuesday2=models.CharField(max_length=200)
    wednesday1=models.CharField(max_length=200)
    wednesday2=models.CharField(max_length=200)
    thurday1=models.CharField(max_length=200)    
    thurday2=models.CharField(max_length=200)    
    friday1=models.CharField(max_length=200)
    friday2=models.CharField(max_length=200)
    saturday1=models.CharField(max_length=200)
    saturday2=models.CharField(max_length=200)