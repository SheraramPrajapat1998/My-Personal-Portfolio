from django.urls import path

from .import views

app_name = 'projects'

urlpatterns = [
  path('', views.project_view, name='project_list'),
  path('tag/<slug:tag_slug>/', views.project_view, name='projects_by_tag'),
  path('<int:year>/<int:month>/<int:day>/<slug:project>/', views.detail_view, name='project_detail'),
]