"""
URL configuration for wall_tracker_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from construction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profiles/<int:profile_id>/days/<int:day>/', views.day_ice_usage, name='day_ice_usage'),
    path('profiles/<int:profile_id>/overview/<int:day>/', views.profile_cost, name='profile_cost'),
    path('profiles/overview/<int:day>/', views.profile_overview, name='profile-overview'),
    path('profiles/overview/', views.overall_cost, name='overall_cost'),
]
