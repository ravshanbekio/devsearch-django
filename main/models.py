from django.db import models
from account.models import Account
from .signals import project_pre_save

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='previews/')
    tag = models.ManyToManyField('Tag',blank=True)
    source = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Developer Projects"

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name

project_pre_save(instance=Project)