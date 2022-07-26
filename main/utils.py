from django.db.models import Q
from .models import Project

def searchProjects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    get_projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(subtitle__icontains=search_query) |
        Q(created_date__icontains=search_query) |
        Q(owner__full_name__icontains=search_query)
    )

    return get_projects, search_query
    