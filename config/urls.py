from django.urls import include, path

urlpatterns = [
    path("api/platform/", include("apps.platform_admin.urls")),
    path("api/tenant/", include("apps.tenant_admin.urls")),
    path("api/portal/", include("apps.user_portal.urls")),
]
