from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('apps.cars.urls')),
    path('accounts/', include('apps.accounts.urls')),
]
