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

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    exclude = ['detail']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    exclude = ['name']