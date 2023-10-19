from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
import django.utils.translation as translation

from .models import Project


def index(request):
    return render(
        request,
        'portfolio/index.html'
    )


def projects(request):
    return render(
        request,
        'portfolio/projects.html',
        {
            'project_list': Project.objects.all()
        }
    )


def contact(request):
    return render(
        request,
        'portfolio/contact.html'
    )


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(
        request,
        'portfolio/project_detail.html',
        {
            'project': project
        }
    )


def set_language(request, lang):
    new_language = 'en'
    if lang in settings.LANGUAGES:
        new_language = lang
    elif lang == 'switch':
        if request.LANGUAGE_CODE == 'en':
            new_language = 'fr'
        else:
            new_language = 'en'

    response = redirect('portfolio:index')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, new_language)
    return response

def set_theme(request, theme):
    new_theme = 'dark'
    if theme in settings.THEMES:
        new_theme = theme
    elif theme == 'switch' and 'theme' in request.COOKIES.keys():
        if request.COOKIES['theme'] == 'dark':
            new_theme = 'light'
        else:
            new_theme = 'dark'

    response = redirect('portfolio:index')
    response.set_cookie('theme', new_theme)
    return response
