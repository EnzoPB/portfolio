from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('project/<int:project_id>', views.project_detail, name='project detail')
]