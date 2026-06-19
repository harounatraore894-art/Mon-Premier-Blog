from django.urls import path
from . import views


urlpatterns  = [
    path('', views.post_list1, name='post_list1'),
]