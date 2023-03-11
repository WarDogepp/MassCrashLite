
from django.contrib import admin
from django.urls import path
from .views import save_location

urlpatterns = [
    path('api/save-location/', save_location),
]
urlpatterns = [
    path('admin/', admin.site.urls),
]
