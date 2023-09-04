from django.contrib import admin

# Register your models here.
from .models import Film, Purchase

admin.site.register(Film)
admin.site.register(Purchase)

class FilmAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'actors')
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('film', 'phone_number', 'email', 'amount', 'purchase_date ', 'link_id')