from django.contrib import admin
from .models import Guest, Cottage, Reservation, Review

# Register your models here.

admin.site.register(Guest)
admin.site.register(Cottage)
admin.site.register(Reservation)
admin.site.register(Review)
