from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, UserChangeForm, SkillForm, ProjectForm
from account.models import Account, Project, Tag
from django.core.paginator import Paginator
from .utils import searchDevelopers

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                form.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('signin')
        else:
            form = RegisterUserForm
    return render(request, 'account/signup.html', {'form':form})
    
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signin')    
        
    return render(request, 'account/login.html')

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('signin')
    else:
        return redirect('signin')

def profiles(request):

    get_developers, search_query = searchDevelopers(request)

    paginator_core = Paginator(Account.objects.all(), 1)
    get_page = request.GET.get('page')
    get_developers_page = paginator_core.get_page(get_page)
    nums = "a" * get_developers_page.paginator.num_pages
    context = {
        'get_developers':get_developers,
        'get_developers_page':get_developers_page,
        'nums':nums,
        'search_query':search_query
    }
    return render(request, 'index.html', context)

def profile(request, pk):
    # if request.user.username == username:
    #     return redirect('myprofile',username=request.user.username)
    # else:
    account_query = Account.objects.get(id=pk)
    context = {
        'account_query':account_query
    }

    return render(request, 'profile.html',context)

def myProfile(request, username):

    if request.user.username == username:
        get_account_data = Account.objects.get(username=request.user.username)

        context = {
            'profile':get_account_data
        }
    else:
        return redirect('home')

    return render(request, 'account.html', context)

@login_required(login_url='signin')
def editAccount(request):
    account = request.user
    form = UserChangeForm(instance=account)

    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('myprofile',username=request.user.username)

    else:
        form = UserChangeForm
    return render(request, 'account/edit-profile.html',{'form':form})

@login_required(login_url='signin')
def createSkill(request):
    account = request.user


    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.account = account
            skill.save()   
            return redirect('myprofile', username=request.user.username)

    else:
        form = SkillForm
    return render(request, 'skill-form.html',{'form':form})
        
@login_required(login_url='signin')
def editSkill(request, pk):
    account = request.user
    skill = account.skill.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('myprofile', username=request.user.username)

    else:
        form = SkillForm
    return render(request, 'skill-form.html',{'form':form})

@login_required(login_url='signin')
def deleteSkill(request, pk):
    account = request.user
    skill = account.skill.get(id=pk)
    skill.delete()
    return redirect('myprofile',username=request.user.username)

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