from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.Register.as_view(), name='login'),
]