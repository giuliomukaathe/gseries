from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import uuid
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='media/')
    description = models.TextField(default="GSeries Production")
    actors = models.TextField(default="GSeries Production")
    trailer_file = models.FileField(upload_to='trailers/')  # Store trailers in 'media/trailers/' directory
    film_file = models.FileField(upload_to='films/')  # Store films in 'media/films/' directory
    link_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Unique link ID for the purchased film
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add the price field

    def __str__(self):
        return self.title 


STATUS = ((1, "Pending"), (0, "Complete"))

class Transaction(models.Model):
    # """This model records all the mpesa payment transactions"""
    transaction_no = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    checkout_request_id = models.CharField(max_length=200)
    reference = models.CharField(max_length=40, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=10)
    status = models.CharField(max_length=15, choices=STATUS, default=1)
    receipt_no = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return f"{self.transaction_no}"

class Purchase(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    link_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Unique link ID for the purchased film

    def __str__(self):
        return self.email 


    def generate_film_link(self):
        return f"http://gseriesmediakenya.com/watch/{self.link_id}/"

    def send_purchase_confirmation_email(self):
        film_link = self.generate_film_link()
        subject = f"Film Purchase: {self.film.title}"
        message = render_to_string('films/email_template.html', {'film': self.film, 'film_link': film_link})
        send_mail(subject, '', 'info@gseriesmediakenya.com', [self.email], html_message=message)
