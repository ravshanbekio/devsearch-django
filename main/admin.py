from django.contrib import admin
from .models import Tag, Project, Comment

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Comment)