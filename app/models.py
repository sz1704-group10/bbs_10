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
    name = models.CharField(max_length=32)
    add_time = models.DateTimeField(default=datetime.now)