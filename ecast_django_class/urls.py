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
from authentication.views import login_view, registrationForm, logout_view
from home.views import home_view
from blog.views import blog, view_blog
from tours.views import add_destination, add_district, delete_destination, tour_destinations
from tours.views import tour_destionation_link
from tours.views import a_tour_destination, update_destiantion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('blog/',blog,name='blog'),
    path('blog/<slug:bTitle>',view_blog,name='view_blog'),


    path('tour/destinations',tour_destinations,name='all_destinations'),
    path('tour/destination/<int:id_val>',a_tour_destination, name='a_destination'),
    path('tour/destinations/links',tour_destionation_link, name='destinationlink'),
    path('tour/destinations/add',add_destination,name="add_destination"),
    path('tour/destinations/update/<int:dId>/',update_destiantion,name="update_destination"),
    path('tour/destinations/delete/<int:dId>/',delete_destination,name="delete_destination"),


    path('tour/destinations/district/add/',add_district,name="add_district"),

    path('register/',registrationForm,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
]
