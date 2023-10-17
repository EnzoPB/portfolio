from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('project/<int:project_id>', views.project_detail, name='project detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
