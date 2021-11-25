from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.overview, name="overview"),
    path('validator/', include('validator.urls')),
#     path("validator/", views.validator_fun, name="validator"),
      path("gwf-db/", views.database, name="gwf-db"),
      path("workflow-hierarchy/", views.hierarchy, name="workflow-hierarchy"),
 ]