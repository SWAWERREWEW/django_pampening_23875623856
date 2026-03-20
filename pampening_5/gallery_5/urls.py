from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_page_genshin),
    path('genshin/', views.gallery_page_genshin),
    path('fnaf/', views.gallery_page_fnaf)
]
