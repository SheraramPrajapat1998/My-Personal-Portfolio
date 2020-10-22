from django.contrib import admin

from .models import Skill, OtherSkill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
  list_display = ('name', 'level', 'value', 'order', 'created', 'updated')
  list_filter = ('level', 'value', 'status', 'created', 'updated')
  list_editable = ( 'value', 'order')

@admin.register(OtherSkill)
class OtherSkillAdmin(admin.ModelAdmin):
  list_display = ('name', 'status', 'order')
  list_editable = ('order', 'status')
  list_filter = ('order', 'status')

