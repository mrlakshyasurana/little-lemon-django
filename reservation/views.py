# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>Welcome to the Little Lemon Booking Page!</h1>")
from django.shortcuts import render

def index(request):
    # This renders your booking.html file instead of raw text
    return render(request, 'booking.html')
