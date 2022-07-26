from django.shortcuts import render
from .utils import searchProjects

def projects(request):

    get_projects, search_query = searchProjects(request)

    context = {
        'get_projects':get_projects,
        'search_query':search_query
    }
    return render(request, 'projects.html', context)