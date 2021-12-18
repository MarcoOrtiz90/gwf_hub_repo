from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.load_albacorizer, name="albacorizer"),
    path("jsoncodes/", views.jsoncodes, name="jsoncodes"),
]
