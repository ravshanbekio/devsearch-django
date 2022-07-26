from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('logout/',views.signout, name='signout'),

    path('',views.profiles, name='home'),
    path('<int:pk>/',views.profile, name='profile-detail'),
    path('profile/<str:username>/',views.myProfile, name='myprofile'),

    path('edit/',views.editAccount, name='edit-profile'),

    path('create-skill/',views.createSkill, name='create-skill'),
    path('edit-skill/<int:pk>/',views.editSkill, name='edit-skill'),
    path('delete-skill/<int:pk>',views.deleteSkill, name='delete-skill'),
]