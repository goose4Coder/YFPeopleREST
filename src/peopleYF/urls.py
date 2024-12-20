from django.contrib import admin
from django.urls import path, include
from .api import router

urlpatterns = [
    # path("members/", include("members.urls")),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
]
