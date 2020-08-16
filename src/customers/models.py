from django.db import models
from django.utils import timezone
from django.urls import reverse
# from django.contrib.auth import get_user_model

# from accounts.models import Invite


class Organistion(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    members = models.ManyToManyField('accounts.User', through='Membership', related_name='org_members')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Organistion, self).save(*args, **kwargs)


class Membership(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organistion, on_delete=models.CASCADE)
    invite = models.ForeignKey('accounts.Invite', on_delete=models.CASCADE)
    date_joined = models.DateField()
    # invite_reason = models.CharField(max_length=64)