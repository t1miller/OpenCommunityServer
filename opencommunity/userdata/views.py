from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Following, Inbox, Follower
from . import serializers
from django.http import HttpResponse
import logging
import json

logger = logging.getLogger(__name__)


class FollowingViewset(viewsets.ModelViewSet):
    """
    Return list of people we follow
    """
    queryset = Following.objects.all()
    serializer_class = serializers.FollowingSerializer

    def list(self, request, **kwargs):
        """
        return list of followers
        """
        user = request.query_params.get('user')
        if self.queryset.filter(me=user).count() == 0:
            return Response({'status': 'no following list'})
        else:
            users_followers = Following.objects.get(me=user)
            data = {"id": users_followers.id, "following": users_followers.usernames}
            return Response(data)

    def create(self, request, **kwargs):
        """
        add to follower list
        """
        user = request.data['user']
        person_to_add = request.data['person_to_add']

        if self.queryset.filter(me=user).count() == 0:
            following = Following(me=user, usernames=[person_to_add])
            following.save()
            return Response({'status': 'successfully created follower list'})
        else:
            following = Following.objects.get(me=user)
            following.usernames.append(person_to_add)
            following.save()
            return Response({'status': 'successfully appended to followers list'})

    def retrieve(self, request, pk=None, **kwargs):
        pass

    def update(self, request, pk=None, **kwargs):
        pass

    def partial_update(self, request, pk=None, **kwargs):
        pass

    def destroy(self, request, pk=None, **kwargs):
        """
        remove user from follower list
        """
        # owner = request.data['owner']
        # person_to_remove = request.data['person_to_remove']
        person_to_remove = request.query_params.get('person_to_remove')
        user = request.query_params.get('user')

        if self.queryset.filter(me=user).count() != 0:
            following = Following.objects.get(me=user)
            following.usernames.remove(person_to_remove)
            following.save()
            return Response({'status': 'successfully removed from follower list'})

        return Response({'status': "nothing to delete"})


class InboxViewset(viewsets.ModelViewSet):
    queryset = Inbox.objects.all()
    serializer_class = serializers.InboxSerializer

    def list(self, request, **kwargs):
        """
        :param request:
        :param kwargs:
        :return: list of followers
        """
        person_to_follow = request.query_params.get('person_to_follow')
        if self.queryset.filter(me=person_to_follow).count() == 0:
            return Response({'status': 'no inbox list'})
        else:
            users_followers = Inbox.objects.get(me=person_to_follow)
            data = {"id": users_followers.id, "inbox": users_followers.usernames}
            return Response(data)

    def create(self, request, **kwargs):
        follower = request.data['follower']
        person_to_follow = request.data['person_to_follow']

        if self.queryset.filter(me=person_to_follow).count() == 0:
            inbox = Inbox(me=person_to_follow, usernames=[follower])
            inbox.save()
            return Response({'status': 'successfully created inbox list'})
        else:
            inbox = Inbox.objects.get(me=person_to_follow)
            inbox.usernames.append(follower)
            inbox.save()
            return Response({'status': 'successfully appended to inbox list'})

    def retrieve(self, request, pk=None, **kwargs):
        pass

    def update(self, request, pk=None, **kwargs):
        pass

    def partial_update(self, request, pk=None, **kwargs):
        pass

    def destroy(self, request, pk=None, **kwargs):
        # owner = request.data['owner']
        # person_to_remove = request.data['person_to_remove']
        person_to_remove = request.query_params.get('person_to_remove')
        owner = request.query_params.get('owner')

        if self.queryset.filter(me=owner).count() != 0:
            inbox = Inbox.objects.get(me=owner)
            inbox.usernames.remove(person_to_remove)
            inbox.save()
            return Response({'status': 'successfully removed from follower list'})

        return Response({'status': "nothing to delete"})
        # make = req.query_params.get('make')
        # if make:
        #     self.queryset = uploadobject.objects.filter(make=make)
        #     return self.queryset
        # else:
        #     return self.queryset

    # def post(self, request):
    #     """
    #     Add request to users requests
    #     :param request:
    #     :return:
    #     """
    #     # follower = request.POST.get("me", "")
    #     # who_to_follow = request.POST.get("person_to_follow", "")
    #     json_data = json.loads(request.body)
    #     follower = json_data["follower"]
    #     who_to_follow = json_data["person_to_follow"]
    #
    #     results = Inbox.objects.all().filter(me=who_to_follow)
    #     if results.count() > 0:
    #         followee = Inbox.objects.get(me=who_to_follow)
    #         followee.usernames.append(follower)
    #         followee.save()
    #     else:
    #         followee = Inbox(me=who_to_follow, usernames=[follower])
    #         followee.save()
    #     return HttpResponse("success-POST")
    #
    # def get(self, request):
    #     """
    #     Return users requests
    #     :param request:
    #     :return:
    #     """
    #     # username = request.GET['me']
    #     # queryset = Inbox.objects.filter(username=username)
    #     return HttpResponse("success-GET")

    # def get_queryset(self):
    #     return Inbox.objects.filter(me=self.request.GET.get("me", ""))


class FollowerViewset(viewsets.ModelViewSet):
    """
    Return list of people who follow us
    """
    queryset = Follower.objects.all()
    serializer_class = serializers.FollowingSerializer


# def addFollower(request):
#     """
#     POST - add a follower
#     GET - get list of followers
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         # # check if user exists
#         # requestor = request.POST.get("who", "")
#         # follower = Follower.objects.get("name")
#         #
#         # jsonFollower = follower.usernames
#         # followers += "me"
#         # followers.save()
#         return HttpResponse("success")


# class RequestViewset(viewsets.ModelViewSet):
#     """
#     Submit a follow request
#     """
# #
# #     def post(self, request):
# #         existingFollowerList = Requests.objects.get("name")
# #         existingFollowerList += "me"
# #         existingFollowerList.save()
# #         return HttpResponse("success")
#     queryset = Requests.objects.all()
#     serializer_class =
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('This is GET request')
#
#     def post(self, request, *args, **kwargs):
#         existingFollowerList = Requests.objects.get("name")
#         existingFollowerList += "me"
#         existingFollowerList.save()
#         return HttpResponse("success")
"""
Django queries 
ChargeSummary.object.filter(month=datetime(year=2015, month=5, day=1, tzinfo=utc))
ChargeSummary.object.filter(job__name='Test Job')
ChargeSummary.object.filter(user__profile__email='irwen@rescale.com')
"""
