from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    def send_follow_request(self, user_id):
        user = CustomUser.objects.get(id=user_id)
        aal_objects = AwaitingApprovalList.objects
        if (not aal_objects.filter(requesting_user=self, requested_user=user).exists()):
            aal_objects.create(requesting_user=self, requested_user=user)

    def approve_follow_request(self, follow_request_id):
        instance = AwaitingApprovalList.objects.get(id=follow_request_id)
        requested_user = instance.requested_user
        FollowingList.objects.create(following_user=self, followed_user=requested_user)
        instance.delete()

    def reject_follow_request(self, follow_request_id):
        instance = AwaitingApprovalList.objects.get(id=follow_request_id)
        instance.delete()


class AwaitingApprovalList(models.Model):
    requesting_user = models.ForeignKey("customuser.CustomUser", related_name="requesting_user", on_delete=models.CASCADE)
    requested_user = models.ForeignKey("customuser.CustomUser", related_name="requested_user", on_delete=models.CASCADE)
    request_date = models.DateTimeField(_("request_date"), auto_now_add=True)


class FollowingList(models.Model):
    following_user = models.ForeignKey("customuser.CustomUser", related_name="following_user",on_delete=models.CASCADE)
    followed_user = models.ForeignKey("customuser.CustomUser", related_name="followed_user", on_delete=models.CASCADE)
    created_date = models.DateTimeField(_("created_date"), auto_now_add=True)
