from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from django.views import defaults as default_views
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="My service API",
        default_version='v1',
        description=" My description",
        terms_of_service="https://www.mysite.com/policies/terms/",
        contact=openapi.Contact(email="my_contact@snippets.local"),
        license=openapi.License(name="My License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),

    # path to user register end points
    path('users/', include('users.urls')),
    path('locations/', include('attractions.urls')),
    path('tour/', include('travel.urls')),
]