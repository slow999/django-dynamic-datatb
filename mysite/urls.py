"""
URL configuration for mysite project.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', include('django_dyn_dt.urls')),  # <-- NEW: API routing rules
]
