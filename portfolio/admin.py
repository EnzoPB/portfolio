from django.contrib import admin

from .models import *

admin.site.site_header = 'Administration enzopb.me'

class LinkInline(admin.TabularInline):
    model = ProjectLink
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    list_display = ['title', 'short_description']
    search_fields = ['title', 'description']
    filter_horizontal = ['skills']
    exclude = ['description', 'short_description']

admin.site.register(ProjectSkill)