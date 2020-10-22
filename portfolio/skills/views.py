from django.shortcuts import render

from .models import Skill, OtherSkill

def skills(request):
  skills = Skill.published.all()
  other_skills = OtherSkill.published.all()

  context = {
    'skills': skills,
    'other_skills': other_skills,
    'skill': 'active',
  }
  return render(request, 'skills/skill.html', context)