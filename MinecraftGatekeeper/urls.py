from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from MinecraftGatekeeper.RootSite.views import ProfileView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^login/$', TemplateView.as_view(template_name="auth/login.html")),
    url(r'^logout/$', 'MinecraftGatekeeper.RootSite.views.logout', name='logout'),

    url(r'^resources/$', login_required(TemplateView.as_view(template_name="resources.html")), name='resources'),

    url(r'^$', login_required(ProfileView.as_view()), name='profile'),
)
