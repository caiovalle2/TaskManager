from django.urls import path
from .views import *

urlpatterns = [
    path('login', loginview),
    path('user/create', createuserview),
    path('api/login', LoginApiView.as_view()),

]