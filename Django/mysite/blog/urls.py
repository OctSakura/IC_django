from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog/',views.blog),
    path('blog/add/',views.add)
]