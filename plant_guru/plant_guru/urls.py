from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
]
