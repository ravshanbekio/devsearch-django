from django import forms
from .models import Project, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','subtitle','description','preview_image','tag','source')
        exclude = ['owner']

        labels = {
            'title':'',
            'subtitle':'',
            'description':'',
            'preview_image':'',
            'tag': '',
            'source':'',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Project name'}),
            'subtitle': forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Short description'}),
            'description': forms.Textarea(attrs={'class':'input input--textarea', 'placeholder':'Description'}),
            'preview_image': forms.FileInput(attrs={'class':'input input--file', 'placeholder':'Project preview image'}),
            'tag': forms.CheckboxSelectMultiple(),
            'source': forms.URLInput(attrs={'class':'input input--url', 'placeholder':'Project source', 'type':'url'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        exclude = ['account','project']

        labels = {
            'comment':'',
        }

        widgets = {
            'comment': forms.Textarea(attrs={'class':"input input--textarea", 'name':"message", 'id':"formInput#textarea", 
            'placeholder':"Write your comments here..."})
        }