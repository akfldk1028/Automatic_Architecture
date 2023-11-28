from django.urls import path
from . import views


urlpatterns = [
    path("", views.MySpatial.as_view()),
]
