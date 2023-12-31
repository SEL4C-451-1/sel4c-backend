"""
Mapeo de URL para Metodologia (Actividades y Preguntas)
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from methodology import views


router = DefaultRouter()
router.register('activities', views.ActivityViewSet)
router.register('formsquestions', views.FormsQuestionViewSet)

app_name = 'methodology'

urlpatterns = [
    path('', include(router.urls)),
    path('sub-activities/<int:parent_activity_id>/', views.SubActivityView.as_view(), name='sub-activities'),  # noqa
]
