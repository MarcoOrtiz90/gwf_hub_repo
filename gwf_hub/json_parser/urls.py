from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.json_parser, name="json_parser"),
    path("parsed_files/", views.call_parser, name="parsed_files")
]