from django.contrib import admin
from django.urls import path

from .views import index, get, create, update, scrape

urlpatterns = [
    path('', index, name="home"),
    path('list', get, name="scrapper-list"),
    path('create', create, name="scrapper-create"),
    path('update/<int:pk>/', update, name="scrapper-update"),
    path('scrape/<int:pk>/', scrape, name="scrape"),
]
