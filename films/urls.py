from django.urls import path
from . import views


app_name = 'films'

urlpatterns = [
    path('', views.film_detail, name='film_detail'),
    path('watch/<int:film_id>/', views.watch_trailer, name='watch_trailer'),
    path('buy/<int:film_id>/', views.buy_film, name='buy_film'),
    path('payment/<int:film_id>/', views.payment_page, name='payment_page'),
    path('success/', views.success_page, name='success_page'),
    path("checkout/", views.MpesaCheckoutView.as_view(), name="checkout"),
    path("callback/", views.MpesaCallBackView.as_view(), name="callback"),

]
