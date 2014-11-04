from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from MinecraftGatekeeper.RootSite.forms import UserChangeForm
from MinecraftGatekeeper.RootSite.models import User


@admin.register(User)
class UserAdmin(OldUserAdmin):
    form = UserChangeForm

    fieldsets = OldUserAdmin.fieldsets + (
        (None, {'fields': (
            'minecraft_username',
            'referred_by',
            'granted_access',
            'suspended_until',
            'suspended_reason',
            'is_operator',
            'can_invite_new_users',
            'reddit_username',
            'reddit_access_granted',
        )}),
    )
