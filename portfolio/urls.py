from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('project/<int:project_id>', views.project_detail, name='project detail'),
    path('set_language/<str:lang>', views.set_language, name='set language'),
    path('set_theme/<str:theme>', views.set_theme, name='set theme')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
