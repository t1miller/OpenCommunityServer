from django.contrib import admin
from .models import Follower, Following, Inbox, Thread

# register models
admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(Inbox)
admin.site.register(Thread)



