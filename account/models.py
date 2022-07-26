from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .signals import project_pre_save

class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have an Username")
        if not email:
            raise ValueError("Users must have an Email")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):

    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    username = models.CharField(max_length=50, unique=True)
    direction = models.CharField(verbose_name=' ',max_length=90, blank=True)
    bio = models.TextField(max_length=400, blank=True)
    address = models.CharField(max_length=80, blank=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True, default='avatars/IMG_20220114_104710_103.JPG')
    date_joined = models.DateTimeField(verbose_name='Date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login',auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = AccountManager()

    class Meta:
        verbose_name_plural = "Users profile"
    
    def __str__(self):
        return self.email

    # def get_skills(self):
    #     return self.skill_set.all()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

class Skill(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='skill')
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    level = models.IntegerField(default=20, help_text="Maximum 100%")
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    is_softskill = models.BooleanField(help_text='Is softskill?')

    class Meta:
        verbose_name_plural = "Skill"

    def __str__(self):
        return self.name

class Project(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='previews/')
    source = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Developer Projects"

    def __str__(self):
        return self.title

project_pre_save(instance=Project)