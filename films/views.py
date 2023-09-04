from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Film, Purchase
from django.http import JsonResponse
from .forms import MpesaCheckoutForm
from .util import MpesaGateWay

import json
import logging
from django.http import JsonResponse
from django.views import View
# from .serializers import MpesaCheckoutSerializer
from .util import MpesaGateWay


# Create your views here.
def film_detail(request):
    films = Film.objects.all()  
    print(films)
    return render(request, 'films/films.html', {'films': films})

def watch_trailer(request, film_id):
    film = Film.objects.get(pk=film_id)
    return render(request, 'films/watch_trailer.html', {'film': film})

def buy_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    return render(request, 'films/buy_film.html', {'film': film})

def payment_page(request, film_id):
    film = Film.objects.get(pk=film_id)

    if request.method == 'POST':
        form = MpesaCheckoutForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            amount = film.price  # 'price' attribute
            expected_amount = film.price

            if amount == expected_amount:
                purchase = Purchase.objects.create(
                    film=film, email=email, phone_number=phone_number, amount=amount
                )
                
                mpesa_gateway = MpesaGateWay()
                payload = {
                    'request': request,
                    'data': {
                        'phone_number': phone_number,
                        'amount': amount,
                        'description': f"Payment for {film.title}",
                    }
                }
                response_data = mpesa_gateway.stk_push_request(payload)
                
                # Process the response and redirect accordingly
                # For example, if successful:
                return redirect('/films/success/')

    else:
        form = MpesaCheckoutForm()

    return render(request, 'films/payment_page.html', {'film': film, 'form': form})

def success_page(request):
    return render(request, 'films/success_page.html')

# ------------------mpesa---------------------------------------------- 
gateway = MpesaGateWay()

class MpesaCheckoutView(View):
    def post(self, request, *args, **kwargs):
        data = {
            "phone_number": request.POST.get("phone_number"),
            "amount": request.POST.get("amount"),
            # Add other required fields
        }
        payload = {"data": data, "request": request}
        res = gateway.stk_push_request(payload)
        return JsonResponse(res, status=200)


class MpesaCallBackView(View):
    def get(self, request):
        return JsonResponse({"status": "OK"}, status=200)

    def post(self, request, *args, **kwargs):
        logging.info("{}".format("Callback from MPESA"))
        data = request.body
        return JsonResponse(gateway.callback(json.loads(data)))