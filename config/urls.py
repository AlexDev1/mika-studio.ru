from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView, DetailView
from rest_framework.authtoken.views import obtain_auth_token

from mika_studio.settings.models import Service

urlpatterns = [path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
               path("newyear/", TemplateView.as_view(template_name="pages/newyear.html"), name="newyear"),
               path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
               path("contacts/", TemplateView.as_view(template_name="pages/contacts.html"), name="contacts"),
               path("service/<int:pk>/", DetailView.as_view(
                       template_name="services/detail.html",
                       model=Service
                   ), name="service-detail"
               ),
               path("photos/", TemplateView.as_view(template_name="pages/photos.html"), name="photos"),
               path("rules/visiting/", TemplateView.as_view(template_name="pages/rules_visiting.html"), name="home"),
               path("rules/pay/", TemplateView.as_view(template_name="pages/rules_pay.html"), name="home"),

               path("rules/ban/", TemplateView.as_view(template_name="pages/rules_ban.html"), name="home"),
               # Django Admin, use {% url 'admin:index' %}
               path(settings.ADMIN_URL, admin.site.urls),
               path('tinymce/', include('tinymce.urls')),
               # User management
               path("users/", include("mika_studio.users.urls", namespace="users")),
               path("accounts/", include("allauth.urls")),
               # path('reviews/', include('reviews.urls')),
               # Your stuff: custom urls includes go here
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
