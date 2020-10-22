from django.db import models

STATUS_CHOICES = (
  ('draft', 'Draft'),
  ('published', 'Published'),
)

SKILL_CHOICES = (
  ('medium', 'Medium'),
  ('advance', 'Advance'),
  ('expert', 'Expert'),
)

class SkillManager(models.Manager):
  def get_queryset(self):
    queryset = super().get_queryset().filter(status='published').order_by('order')
    return queryset

class Skill(models.Model):
  name    = models.CharField(max_length=70)
  level   = models.CharField(max_length=20, choices=SKILL_CHOICES, default='Medium')
  value   = models.IntegerField(default=50, help_text='Please add a value between 0 to 100')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status  = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Published')
  order   = models.PositiveIntegerField(blank=False, null=False)

  objects   = models.Manager() # The default manager
  published = SkillManager() # The custom manager
   
  class Meta:
    ordering = ('-order', '-value', 'level')
  
  def __str__(self):
    return f"{self.name}, level {self.level} and value {self.value}"


class OtherSkill(models.Model):
  name    = models.CharField(max_length=250) 
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status  = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Published')
  order   = models.PositiveIntegerField()
  
  objects   = models.Manager() # The default manager
  published = SkillManager() # The custom manager

  def __str__(self):
    return f"{self.name}"