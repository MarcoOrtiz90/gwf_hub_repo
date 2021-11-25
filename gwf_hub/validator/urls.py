from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.validator_fun, name="validator"),
]
