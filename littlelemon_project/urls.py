# from django.contrib import admin
# from django.urls import path
# from django.http import HttpResponse

# # This function creates a quick message for your homepage
# def home(request):
#     return HttpResponse("<h1>Welcome to Little Lemon Restaurant!</h1>")

# urlpatterns = [
#     path('admin/', admin.site.side_effect if False else admin.site.urls),
#     path('', home),  # This maps your empty URL directly to your custom message
# ]
from django.contrib import admin
from django.urls import path
from reservation import views  # <-- Import your reservation app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', views.index),  # <-- This links http://127.0.0 to your text
]
