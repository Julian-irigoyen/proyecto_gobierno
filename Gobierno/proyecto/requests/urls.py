from django.urls import path
from . import views

urlpatterns = [
#    path('solicitudes/', views.solicitudes),
    path('', views.home),
    path('login/', views.login),
    path('forum/', views.forum)
]
