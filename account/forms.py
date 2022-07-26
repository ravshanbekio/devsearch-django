from django import forms
from .models import Account, Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input input--password', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input input--password','placeholder':'Password confirmation'}))

    class Meta:
        model = Account
        fields = ('full_name','email','username')

        labels = {
            'full_name': '',
            'email': '',
            'username': '',
        }

        widgets = {
            'full_name':forms.TextInput(attrs={'class':"input input--text", 'id':"formInput#text", 'type':"text", 'name':"text", 'placeholder':"e.g. Ravshanbek Madaminov"}),
            'email':forms.EmailInput(attrs={'class':"input input--email", 'id':"formInput#email", 'type':"email", 'name':"email", 'placeholder':"e.g. user@domain.com"}),
            'username': forms.TextInput(attrs={'class':"input input--text", 'id':"formInput#text", 'type':"text", 'name':"text", 'placeholder':"e.g. ravshanbeck"})
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('full_name','email','username','direction','bio','address','avatar')

        labels = {
            'full_name':'',
            'email':'',
            'username':'',
            'direction':'',
            'bio':'',
            'address':'',
            'avatar':''
        }

        widgets = {
            'full_name':forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Full name'}),
            'email':forms.EmailInput(attrs={'class':'input input--email', 'placeholder':'Email address'}),
            'username': forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Username'}),
            'direction': forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Direction'}),
            'bio': forms.Textarea(attrs={'class':'input input--textarea', 'placeholder':'Bio'}),
            'address':forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Address'}),
            'avatar':forms.FileInput(attrs={'class':'input input--file', 'placeholder':'Profile photo'})
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name','description','level','is_softskill')
        exclude = ['account']

        labels = {
            'name':'',
            'description': '',
            'level':'',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'input input--text', 'placeholder':'Skill name'}),
            'description':forms.Textarea(attrs={'class':'input input--text', 'placeholder':'Skill description'}),
            'level':forms.NumberInput(attrs={'class':"input input--number", 'placeholder':'Skill level (in percent)'}),
        }