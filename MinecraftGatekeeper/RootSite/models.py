from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    minecraft_username = models.CharField(max_length=120, blank=True)
    referred_by = models.CharField(max_length=120, blank=True)  # This should be Minecraft username.
    granted_access = models.BooleanField(default=False)
    suspended_until = models.DateTimeField(blank=True, null=True)
    suspended_reason = models.CharField(max_length=140, blank=True)
    is_operator = models.BooleanField(default=False)
    can_invite_new_users = models.BooleanField(default=False)
    reddit_username = models.CharField(max_length=120, blank=True, default='')
    reddit_access_granted = models.BooleanField(default=False)
