from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic import FormView, UpdateView
from MinecraftGatekeeper.RootSite.forms import ProfileForm
from MinecraftGatekeeper.RootSite.models import User


def logout(request):
    auth_logout(request)
    return redirect('/login/')


class ProfileView(FormView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = '/'

    def form_valid(self, form):
        form.update_profile()
        return super(ProfileView, self).form_valid(form)
