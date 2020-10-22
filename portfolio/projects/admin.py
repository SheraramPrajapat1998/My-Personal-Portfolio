from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin
from .models import Project, Images

class ImagesAdminInline(AdminImageMixin, admin.StackedInline):
  model = Images

@admin.register(Project)
class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
  list_display = ('title', 'order','created', 'publish')
  list_filter = ('status', 'created', 'updated', 'publish')
  list_editable = ('order', )
  prepopulated_fields = {'slug': ('title',)}
  search_fields = ('title', 'description', 'github_link')
  date_hierarchy = 'created'
  inlines = [ImagesAdminInline]
  ordering = ('-publish', '-order')
