from django.urls import path
from . import views
from .views import (CustomLoginView, CustomLogoutView, CustomUserCreateView,
                    MessageListView,CustomUserListCreate, MessageListCreate)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('api/users/', CustomUserListCreate.as_view(), name='user-list'),
    path('api/messages/', MessageListCreate.as_view(), name='message-list'),
]