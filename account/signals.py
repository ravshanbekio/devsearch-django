from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings

@receiver(pre_save, sender=settings.PROJECT_MODEL)
def project_pre_save(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()