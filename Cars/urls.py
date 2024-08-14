from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mercedes/', views.mercedes, name='mercedes'),
    path('lamborgini/', views.lamborgini, name='lamborgini'),
    path('ferrari/', views.ferrari, name='ferrari'),
]
