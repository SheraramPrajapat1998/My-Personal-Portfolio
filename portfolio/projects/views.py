from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from .models import Project, Images

def project_view(request, tag_slug=None):
  projects = Project.published.all()

  tag = None
  if tag_slug:
    tag = get_object_or_404(Tag, slug=tag_slug)
    projects = projects.filter(tags__in=[tag])
  context = {
    'projects':projects, 
    'tag':tag, 
    'project_active':'active'
  }
  return render(request, 'projects/list.html', context)

def detail_view(request, year, month, day, project):
  project = get_object_or_404(Project, slug=project, status='published', publish__year=year, publish__month=month, publish__day=day)
  images = project.other_images.all()     # returns queryset of other images for a project
  context = {'project': project, 'images':images, 'project_active':'active'}
  return render(request, 'projects/detail.html', context)

