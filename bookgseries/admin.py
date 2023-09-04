
from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'county', 'package', 'booking_date') 

admin.site.register(Booking, BookingAdmin)