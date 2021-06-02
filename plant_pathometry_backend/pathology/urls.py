from django.urls import path

from pathology.views.plant import PlantView

urlpatterns = [
    path('plant/', PlantView.as_view(), name = 'plant'),
]
