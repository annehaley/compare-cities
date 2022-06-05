from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cities.rest import CityViewSet


# OpenAPI generation
schema_view = get_schema_view(
    openapi.Info(title="Cities", default_version="v1", description=""),
    public=True,
)

router = routers.SimpleRouter(trailing_slash=False)


for model_name, viewset in [
    ("cities", CityViewSet),
]:
    router.register(f"{model_name}", viewset, basename=model_name)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/docs/redoc/", schema_view.with_ui("redoc"), name="docs-redoc"),
    path("api/docs/swagger/", schema_view.with_ui("swagger"), name="docs-swagger"),
]
