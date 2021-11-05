from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email

class chemicals(models.Model):
    Tempchoice = (('RT','RT'),('4','4'),('-20','-20'))
    name = models.CharField(max_length=20)
    vender = models.CharField(max_length=20)
    CAT = models.CharField(max_length=20,default='ABCD')
    LOT = models.CharField(max_length=20,default='ABCD')
    temperature = models.CharField(max_length=20, choices=Tempchoice, default='RT')
    experiment = models.CharField(max_length=15)
    arrive_date = models.DateField()
    expire_date = models.DateField()
    operator = models.CharField(max_length=20,default='ABCD')
    #agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    def __str__(self):
        return self.name





