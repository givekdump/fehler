from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

from PIL import Image


class Organistion(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Organistion, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    organisation = models.ManyToManyField(Organistion)
    #project = models.ManyToManyField(Project, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    def save(self):
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)