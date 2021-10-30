from django.urls import path

from .views import get_all

urlpatterns = [
    path('all/', get_all, name="all"),
    path(),
]