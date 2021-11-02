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
    name = models.CharField(max_length=20)
    vender = models.CharField(max_length=20)
    experiment = models.CharField(max_length=15)
    arrive_date = models.DateField()
    expire_date = models.DateField()
    #agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    def __str__(self):
        return self.name





