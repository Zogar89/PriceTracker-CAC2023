from django.contrib import admin
from django.urls import path, include
from home import views as views_home

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('' , views_home.index),
    path('home/', include('home.urls')),
]
