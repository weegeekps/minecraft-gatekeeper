from django.contrib.auth.forms import UserChangeForm as OldUserChangeForm
from MinecraftGatekeeper.RootSite.models import User


class UserChangeForm(OldUserChangeForm):
    class Meta(OldUserChangeForm.Meta):
        model = User
