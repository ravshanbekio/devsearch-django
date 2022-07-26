from django.shortcuts import render, get_object_or_404
from .utils import searchProjects
from account.models import Project

def projects(request):

    get_projects, search_query = searchProjects(request)

    context = {
        'get_projects':get_projects,
        'search_query':search_query
    }
    return render(request, 'projects.html', context)

def project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    context = {
        'project':project
    }

    return render(request, 'single-project.html', context)