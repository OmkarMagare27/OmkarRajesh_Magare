# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Contact
from .forms import ContactForm

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})

def landing_page(request):
    return render(request, 'contacts/landing_page.html')

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})

def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update_contact.html', {'form': form})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('list_contacts')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})

