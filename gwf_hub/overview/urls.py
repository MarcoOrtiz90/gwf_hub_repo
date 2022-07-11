from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.overview, name="overview"),
    path('validator/', include('validator.urls')),
    path('auto-answer-generator/', include('auto_answer_generator.urls')),
    path("gwf-db/", views.database, name="gwf-db"),
    path("workflow-hierarchy/", views.hierarchy, name="workflow-hierarchy"),
    path("albacorizer/", include('albacorizer.urls')),
    path('json_parser/', include('json_parser.urls')),
    path('payload_builder', include('payload_builder.urls')),
    path('task_extractor/', include('paramount_task_extractor.urls'))
 ]

