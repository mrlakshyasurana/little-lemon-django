from django.contrib import admin
from django.urls import path
from reservation import views  # Import your reservation views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', views.index),          # Your booking form page
    path('bookings-list/', views.bookings_list), # Your new summary list page
]
