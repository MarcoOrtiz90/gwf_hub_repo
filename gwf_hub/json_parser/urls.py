from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.call_parser, name="json_parser")
]
