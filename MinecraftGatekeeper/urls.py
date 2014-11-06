from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required, permission_required
from MinecraftGatekeeper.RootSite.views import ProfileView, ManageListView, ManageDetailView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^login/$', TemplateView.as_view(template_name="auth/login.html")),
    url(r'^logout/$', 'MinecraftGatekeeper.RootSite.views.logout', name='logout'),

    url(r'^resources/$', login_required(TemplateView.as_view(template_name="resources.html")), name='resources'),

    url(r'^manage/$', permission_required('RootSite.change_user')(ManageListView.as_view()), name='manage-list'),
    url(r'^manage/(?P<slug>\w+)/$', permission_required('RootSite.change_user')(ManageDetailView.as_view()), name='manage-detail'),

    url(r'^$', login_required(ProfileView.as_view()), name='profile'),
)
