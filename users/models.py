from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    progress = models.JSONField(default=dict, blank=True)
    google_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.email or self.username
