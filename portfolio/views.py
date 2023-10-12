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
        'portfolio/projects.html'
    )

def contact(request):
    return render(
        request,
        'portfolio/contact.html'
    )
