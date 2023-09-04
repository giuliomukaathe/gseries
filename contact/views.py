
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the model
            form.save()
            return render(request, 'contact/contact_success.html')  # Render the success template
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
