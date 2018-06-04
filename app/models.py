from datetime import datetime

from django.db import models

# Create your models here.
class BBS(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    user_id = models.IntegerField(null=True)
    add_time = models.DateTimeField(default=datetime.now)
    def getUser(self):
        user = User.objects.filter(id=self.user_id).first()
        return user

class User(models.Model):
    SEX = (
        ('1','男'),
        ('2','女'),
        ('3','保密'),
    )
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=128,default='')
    images = models.ImageField(upload_to='icon/',max_length=128,default='icon/default.jpeg')
    sex = models.CharField(choices=SEX,max_length=32,default='1')
    age = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)