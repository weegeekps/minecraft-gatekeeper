from django.contrib import auth, messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic import FormView, ListView, DetailView, UpdateView, View, RedirectView
from MinecraftGatekeeper.RootSite.forms import ProfileForm, UserChangeForm, SuspendUserForm


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


class ManageDetailView(DetailView):
    template_name = 'manage/detail.html'
    model = auth.get_user_model()
    slug_field = 'username'


class SuspendUserView(FormView):
    template_name = 'manage/suspend.html'
    form_class = SuspendUserForm

    def get_initial(self):
        user = auth.get_user_model().objects.get(username=self.kwargs['slug'])

        return {
            'suspended_reason': user.suspended_reason,
            'suspended_until': user.suspended_until,
        }

    def form_valid(self, form):
        user = auth.get_user_model().objects.get(username=self.kwargs['slug'])
        user.suspended_reason = form.cleaned_data['suspended_reason']
        user.suspended_until = form.cleaned_data['suspended_until']
        user.save()

        messages.success(self.request, 'User has been suspended successfully.')

        return super(SuspendUserView, self).form_valid(form)

    def get_success_url(self):
        return reverse('manage-detail', kwargs={'slug': self.kwargs['slug']})


class UnsuspendUserView(RedirectView):
    permanent = False
    pattern_name = 'manage-detail'

    def get_redirect_url(self, *args, **kwargs):
        user = auth.get_user_model().objects.get(username=self.kwargs['slug'])
        user.suspended_reason = ''
        user.suspended_until = None
        user.save()

        messages.success(self.request, 'User has been unsuspended.')

        return super(UnsuspendUserView, self).get_redirect_url(*args, **kwargs)
