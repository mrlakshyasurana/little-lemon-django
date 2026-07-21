from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking

def index(request):
    if request.method == 'POST':
        # Grab data from the HTML form inputs
        name = request.POST.get('first_name')
        date = request.POST.get('reservation_date')
        seats_count = request.POST.get('seats')

        # Save data into the Booking database table
        booking_entry = Booking(
            first_name=name,
            reservation_date=date,
            seats=seats_count
        )
        booking_entry.save()

        # Send a success confirmation text back
        return HttpResponse(f"<h1>Thank you {name}! Your booking for {seats_count} seats is confirmed.</h1>")
        
    # If it's a regular page load (GET request), just show the empty form
    return render(request, 'booking.html')

def bookings_list(request):
    all_bookings = Booking.objects.all()
    return render(request, 'bookings_list.html', {'bookings': all_bookings})

