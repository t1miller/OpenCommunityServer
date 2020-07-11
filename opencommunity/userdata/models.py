from django.db import models
from django_mysql.models import JSONField


class Follower(models.Model):
    me = models.CharField(max_length=128, null=False)
    usernames = JSONField()


class Following(models.Model):
    me = models.CharField(max_length=128, null=False)
    usernames = JSONField()


class Inbox(models.Model):
    me = models.CharField(max_length=128, null=False)
    usernames = JSONField()


class Thread(models.Model):
    creator = models.CharField(max_length=128, null=False)
    radius = models.PositiveIntegerField()
    gpsCoordinate = JSONField()
    isGpsExact = models.BooleanField()
    isPostPublic = models.BooleanField()
    category = models.CharField(max_length=128, null=False)
    expirationHours = models.PositiveIntegerField()
    creationTime = models.DateTimeField()
    message = models.TextField()


# class UserData(models.Model):
#     threads = ArrayField(Thread)
#     followers = ArrayField(Follower)
#     following = ArrayField(Following)
#     requests = ArrayField(Requests)



#     user=models.ForeignKey(User,on_delete=models.CASCADE)
