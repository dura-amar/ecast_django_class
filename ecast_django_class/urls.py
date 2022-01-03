"""ecast_django_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import home_view
from blog.views import blog
from tours.views import tour_destinations
from tours.views import a_tour_destination

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('blog/',blog,name='blog'),
    path('tour/destinations',tour_destinations,name='all_destinations'),
    path('tour/destination/<int:id_val>',a_tour_destination, name='a_destination'),
]
