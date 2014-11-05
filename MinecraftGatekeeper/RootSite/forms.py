from django import forms
from django.contrib.auth.forms import UserChangeForm as OldUserChangeForm
from MinecraftGatekeeper.RootSite.models import User


class UserChangeForm(OldUserChangeForm):
    class Meta(OldUserChangeForm.Meta):
        model = User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'minecraft_username', 'referred_by', 'reddit_username']

    def update_profile(self):
        # This is where we will update the profile.
        pass
