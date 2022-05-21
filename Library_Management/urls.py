from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import *
# from home.apis.viewsets import ChangePasswordViewset
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
