from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils.translation import gettext

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