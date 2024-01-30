from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookbook_api/', include('cookbook_api.urls')),
    path('recipes/', include('recipes.urls')),
]
