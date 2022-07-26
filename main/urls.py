from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.projects, name='projects'),
    path('project/<slug:slug>/',views.project, name='project-detail'),

    path('create-project/',views.createProject, name='create-project'),
    path('edit-project/<slug:slug>/',views.editProject, name='edit-project'),
    path('delete-project/<slug:slug>/',views.deleteProject, name='delete-project'),
]