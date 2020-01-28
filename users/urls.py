from django.urls import path

from .views import *


app_name = 'user'

urlpatterns = [
    path('', AllUsersView),
    path('<int:pk>/', UserView),
    path('users/', UsersView.as_view()),
]