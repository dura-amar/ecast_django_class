from django.contrib import admin

from tours.models import Category, Destination, District

# Register your models here.
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Destination)
