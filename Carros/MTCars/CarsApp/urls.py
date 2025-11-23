from django.contrib import admin
from django.urls import path
from CarsApp import views

app_name = "CarsApp"

urlpatterns = [
    path('ranking/', views.ranking_view, name='ranking'),
    path("", views.searchf, name="home"),
]