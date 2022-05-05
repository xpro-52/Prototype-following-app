from django.urls import path
from . import views

app_name = 'customuser'
urlpatterns = [
    path('', views.CustomUserProfileView.as_view(), name='user-profile'),
    path('user-list/', views.CustomUserListView.as_view(), name='user-list'),
    path('send-follow-request/', views.send_follow_request, name='send-follow-request'),
    path('approve-follow-request/', views.approve_follow_request, name='approve-follow-request'),
]






