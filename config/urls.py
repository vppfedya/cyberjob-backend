from django.contrib import admin
from django.urls import path, include # <-- Добавьте include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # <-- ДОБАВЬТЕ ЭТУ СТРОКУ
]