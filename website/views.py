from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from website.forms import LogForm, BookingForm
from django.template import loader


def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request,"home.html",context)

def booking_form_view(request):
     form = BookingForm()
     if request.method == 'POST':
         form = BookingForm(request.POST)
         if form.is_valid():
            form.save()
     context = {"form" : form}
     return render(request, "booking.html", context)

def drinks(request, drink_name):
    drink = {
        'mocha' : 'this is a type of coffee',
        'tea' : 'this is a type of hot beverage',
        'lemonade': 'this is a type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)


def home(request):
    return render(request, 'hello.html', {}) # follows the DRY convention

def about(request):
    return HttpResponse("About Us")

def menu(request):
    return HttpResponse("Menu for Little-Lemon")

