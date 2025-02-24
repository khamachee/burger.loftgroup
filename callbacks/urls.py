from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HandleWebhookAPIView

urlpatterns = [
    path('watch/', HandleWebhookAPIView.as_view()),
]
