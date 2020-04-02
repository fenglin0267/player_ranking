from django.db import models

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=50)



class UserScore(models.Model):
    score = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)