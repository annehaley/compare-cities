from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path
from rest_framework import routers


# OpenAPI generation
schema_view = get_schema_view(
    openapi.Info(title="Cities", default_version="v1", description=""),
    public=True,
)

router = routers.SimpleRouter(trailing_slash=False)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/redoc/", schema_view.with_ui("redoc"), name="docs-redoc"),
    path("api/docs/swagger/", schema_view.with_ui("swagger"), name="docs-swagger"),
]
