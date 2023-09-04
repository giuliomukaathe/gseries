from django.urls import path
from . import views

app_name = 'bookgseries'

urlpatterns = [
    path('', views.book_form, name='book_form'),
    path('success/', views.booking_success, name='booking_success'),
]
