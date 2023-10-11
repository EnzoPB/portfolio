from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils.translation import gettext

from .models import Project


class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    model = Project