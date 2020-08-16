from django.db.models.signals import post_save
from django.dispatch import receiver

from . models import User, Invite, Profile


@receiver(post_save, sender=User)
def deactivate_invite(sender, instance, created, **kwargs):
    if created:
        try:
            invite = Invite.objects.get(email=instance.email)
            invite.is_active = False
            invite.save()
        except Exception:
            pass


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()