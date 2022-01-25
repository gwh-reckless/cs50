from ast import Pass
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.


def index(request):
    flights = Flight.objects.all()
    return render(request, 'flights/index.html', {
        'flights': flights
    })


def flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == 'POST':
        flight = get_object_or_404(Flight, pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)

    return HttpResponseRedirect(reverse('flights:flight', args=(flight.id,)))
