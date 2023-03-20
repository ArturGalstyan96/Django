from django.shortcuts import render, redirect
from .models import Tour, About, Contact
from .forms import ContactForm
# Create your views here.

def home(request):
    Tour_List = Tour.objects.all()
    return render(request, 'main\home.html', context={
        'Tour_List': Tour_List
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactForm()    
    return render(request, 'main\contact.html', context={
        'form': form
    })


def about(request):
    about_list = About.objects.all()
    return render(request, 'main\About.html', context={
        'about_list': about_list
    })

