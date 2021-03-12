from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "mika_studio.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import mika_studio.users.signals  # noqa F401
        except ImportError:
            pass
