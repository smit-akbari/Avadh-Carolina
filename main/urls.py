from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='dashboard_view'),
    path('services_view/', services_view, name='services_view'),
    path('addEvent/', addEvent, name='addEvent'),
    path('delete_event/<int:booking_id>', delete_event, name='delete_event'),
    path('gallery_view/', gallery_view, name='gallery_view'),
    path('events_view/', events_view, name='events_view'),
    path('emergency_contact_view/', emergency_contact_view, name='emergency_contact_view'),
    path('suggestion_view/', suggestion_view, name='suggestion_view'),
]