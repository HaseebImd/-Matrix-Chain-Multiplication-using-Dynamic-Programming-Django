from django.urls import path
from App import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("DynamicProgramming", views.DynamicProgramming, name="DynamicProgramming"),
    ]