# users/serializers.py
from rest_framework import serializers
from . import models


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Follower
        fields = ('usernames', 'me')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Following
        fields = ('usernames', 'me')


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inbox
        fields = ('me', 'usernames')


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thread
        fields = ('creator', 'radius', 'gpsCoordinate', 'isGpsExact', 'isPostPublic',
                  'category', 'expirationHours', 'creationTime', 'message')
