from django.contrib import admin

from customuser.models import AwaitingApprovalList, CustomUser, FollowingList

admin.site.register(CustomUser)
admin.site.register(AwaitingApprovalList)
admin.site.register(FollowingList)
