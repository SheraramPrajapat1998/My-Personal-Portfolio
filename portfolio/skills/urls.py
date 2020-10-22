from django.urls import path
from .import views

app_name = 'skills'

urlpatterns = [
  path('', views.skills, name='skills')
]