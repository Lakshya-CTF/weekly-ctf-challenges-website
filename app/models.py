from django.db import models
from django.contrib.auth.models import AbstractUser
import json 

# Create your models here.

DEPARTMENTS = (('CO','COMPUTER'),('IT','IT'),('ET','ENTC'),('OT','OTHERS'))
YEAR = (('FE','FE'),('SE','SE'),('TE','TE'),('BE','BE'))

class CustomUser(AbstractUser):
	college = models.CharField(max_length=30)
	department = models.CharField(max_length=2,choices=DEPARTMENTS)
	year = models.CharField(max_length=2,choices=YEAR)
	points = models.IntegerField(default=0)



class Question(models.Model):
	qid = models.IntegerField(default=0)
	qtitle = models.CharField(max_length=30,default='challenge')
	flag = models.CharField(max_length=40,default='pict_CTF{}')
	points = models.IntegerField(default=0)
	solved = models.IntegerField(default=0)
	description = models.TextField(default='lorem ipsum')

	def __str__(self):
		return self.qtitle



class SolvedQuestions(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)




