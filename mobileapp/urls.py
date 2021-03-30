from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('logic_1/', logic_1),
    path('logic_1_no/', logic_1_no),
    path('logic_1_no_no/', logic_1_no_no),
    path('logic_2/', logic_2),
    path('logic_2_no/', logic_2_no),
    path('logic_2_yes/', logic_2_yes),
    path('logic_3/', logic_3),
    path('website/', website, name='website'),
    path('save', save),
    path('website/save', save),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),


]