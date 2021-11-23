from django.urls import path
from . import views

urlpatterns = [
    path("", views.overview, name="overview"),
    path("gwf-db/", views.database, name="gwf-db"),
    path("validator/", views.validator_fun, name="validator")
]