from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserChangeForm as OldUserChangeForm


class UserChangeForm(OldUserChangeForm):
    class Meta(OldUserChangeForm.Meta):
        model = auth.get_user_model()


class ProfileForm(forms.Form):
    email = forms.EmailField(required=True, max_length=75)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    minecraft_username = forms.CharField(max_length=120)
    referred_by = forms.CharField(max_length=120, required=False)
    reddit_username = forms.CharField(max_length=120, required=False)

