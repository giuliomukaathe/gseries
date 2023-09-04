
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import BookingForm

def send_confirmation_email(user_email):
    subject = 'Booking Confirmation'
    message = 'Success! You have booked with us. We will contact you soon.'
    from_email = 'info@gseriesmediakenya.com'
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)

def send_booking_email(booking_data):
    subject = 'New Booking Received'
    from_email = 'info@gseriesmediakenya.com'
    recipient_list = [booking_data['email'], 'info@gseriesmediakenya.com']

    # Render the email content using a template
    context = {
        'name': booking_data['name'],
        'email': booking_data['email'],
        'phone_number': booking_data['phone_number'],
        'package': booking_data['package'],
    }
    message = render_to_string('booking/booking_email_template.html', context)

    send_mail(subject, message, from_email, recipient_list, html_message=message)

from django.shortcuts import render, redirect

def book_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            booking_instance = form.save()
            
            # Send emails to admin and user
            send_booking_email(form.cleaned_data)
            send_confirmation_email(form.cleaned_data['email'])
            
            return redirect('bookgseries:booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookgseries/booking.html', {'form': form})

def booking_success(request):
    return render(request, 'bookgseries/success.html')

