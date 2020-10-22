from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

def contact(request):
  form = ContactForm()
  if request.method == 'POST':
    form = ContactForm(data=request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Thank you! Your message has been sent.')
      return redirect('contact:contact')
  return render(request, 'contact/contact.html', {'form':form, 'contact':'active'})