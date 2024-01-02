from django.urls import path
from .views import *

urlpatterns = [
    path('home', home),
    path('user-manager', usuários),
    path('task', task),
    path('api/users/', UsersView.as_view()),
    path('api/user/<int:pk>', UsersView.as_view()),
    path('api/tasks', TaskView.as_view()),
    path('api/task/status/<int:pk>', TaskStatusView.as_view()),


]