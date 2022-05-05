import json
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, AwaitingApprovalList, FollowingList


class CustomUserProfileView(LoginRequiredMixin,
                            generic.TemplateView,):
    template_name = "customuser/customuser_profile.html"

    def get_context_data(self, **kwargs):
        self.extra_context = {
            "awaiting_approval_list": AwaitingApprovalList.objects.filter(
                requesting_user=self.request.user
            ),
            "following_list": FollowingList.objects.filter(
                following_user=self.request.user
            ),
        }
        # print(self.extra_context["awaiting_approval_list"][0].id)
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        # user: CustomUser = request.user
        # user.approve_follow_request(follow_request_id=2)
        return super().get(request, *args, **kwargs)


class CustomUserListView(generic.ListView):
    model = CustomUser
    # def post(self, request):
    #     return redirect(to=reverse('customuser:user-list'))


def send_follow_request(request: HttpRequest):
    user: CustomUser = request.user
    user.send_follow_request(user_id=request.POST.get('user_id'))
    return JsonResponse(data={"a": "a"})


def approve_follow_request(request: HttpRequest):
    user: CustomUser = request.user
    id = request.POST.get('follow_request_id')
    user.approve_follow_request(follow_request_id=id)
    return JsonResponse(data={"a": "a"})