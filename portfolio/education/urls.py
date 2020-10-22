from django.urls import path

from .import views

app_name = 'education'

urlpatterns = [
  path('', views.education_view, name='education'),
]