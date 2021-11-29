from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.json_parser, name="parser"),
]