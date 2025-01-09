from django.urls import path
from .views import PANCardOCRView

urlpatterns = [
    path('process/', PANCardOCRView.as_view(), name='process-pan'),
]
