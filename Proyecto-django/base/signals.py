from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=UserProfile)
def actualizar_id_unico(sender, instance, created, **kwargs):
    if created:
        instance.id_unico = UserProfile.objects.count()
        instance.save()