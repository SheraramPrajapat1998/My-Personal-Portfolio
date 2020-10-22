from django.db import models
from django.utils import timezone
from django.urls import reverse
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager

STATUS_CHOICES = (
  ('draft', 'Draft'),
  ('published', 'Published'),
)

class ProjectManager(models.Manager):
  def get_queryset(self):
    queryset = super().get_queryset().filter(status='published', publish__lte=timezone.now())
    print(queryset)
    return queryset



class Project(models.Model):
  title         = models.CharField(max_length=100)
  slug          = models.SlugField(max_length=100, unique=True)
  image         = ImageField(upload_to='project/') # main image of project for home page
  description   = models.TextField()
  github_link   = models.URLField(blank=True, null=True)
  live_link     = models.URLField(blank=True, null=True)
  created       = models.DateTimeField(auto_now_add=True)
  publish       = models.DateTimeField(default=timezone.now)
  updated       = models.DateTimeField(auto_now=True)
  status        = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Draft')
  order         = models.IntegerField(blank=False, null=False) 

  tags          = TaggableManager() # this will be used to show tools and technology used
  objects       = models.Manager()
  published     = ProjectManager()

  class Meta:
    ordering    = ('-publish', '-updated')
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('projects:project_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
  

class Images(models.Model):
  multi_image = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='other_images')
  image       = ImageField(upload_to='project/')