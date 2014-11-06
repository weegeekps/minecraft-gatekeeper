from django.contrib import auth, messages
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic import FormView, ListView, DetailView, UpdateView
from MinecraftGatekeeper.RootSite.forms import ProfileForm, UserChangeForm


def logout(request):
    auth_logout(request)
    return redirect('/login/')


class ProfileView(FormView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = '/'

    def get_initial(self):
        return {
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'minecraft_username': self.request.user.minecraft_username,
            'referred_by': self.request.user.referred_by,
            'reddit_username': self.request.user.reddit_username,
        }

    def form_valid(self, form):
        user = auth.get_user_model().objects.get(pk=self.request.user.pk)
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.minecraft_username = form.cleaned_data['minecraft_username']
        user.referred_by = form.cleaned_data['referred_by']
        user.reddit_username = form.cleaned_data['reddit_username']
        user.save()

        messages.success(self.request, 'Profile updated successfully.')

        return super(ProfileView, self).form_valid(form)


class ManageListView(ListView):
    template_name = 'manage/list.html'
    model = auth.get_user_model()


class ManageDetailView(UpdateView):
    template_name = 'manage/detail.html'
    model = auth.get_user_model()
    slug_field = 'username'
