from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .utils import searchProjects
from .models import Project, Tag
from .forms import ProjectForm

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

@login_required(login_url='signin')
def createProject(request):

    account = request.user

    if request.method == "POST":
        new_tags = request.POST.get('newtags').replace(','," ").split()
        form = ProjectForm(request.POST or None, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = account
            project.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(tag_name=tag)
                project.tag.add(tag)
            return redirect('myprofile',username=request.user.username)

    else:
        form = ProjectForm
    return render(request, 'project-form.html',{'form':form})

@login_required(login_url='signin')
def editProject(request, slug):
    owner = request.user
    project = owner.projects.get(slug=slug)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST or None, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('myprofile',username=request.user.username)

    else:
        form = ProjectForm
    
    return render(request, 'project-form.html',{'form':form})

@login_required(login_url='signin')
def deleteProject(request, slug):
    account = request.user
    project = account.projects.get(slug=slug)
    project.delete()
    return redirect('myprofile',username=request.user.username)