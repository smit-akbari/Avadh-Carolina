from django.shortcuts import render
from datetime import datetime


# Create your views here.
def dashboard_view(request):
     # Get the current time
    current_time = datetime.now().time()

    # Define greeting messages based on the time of day
    if current_time.hour < 12:
        greeting = 'Good morning'
    elif current_time.hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'

     # Get the user's name (you can replace 'John' with the actual user's name)
    user_name = 'John'

    # Pass the greeting and user_name to the template
    context = {
        'greeting': greeting,
        'user_name': user_name,
    }
    return render(request, 'dashboard.html', context)

def services_view(request):
    return render(request, 'services.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def events_view(request):
    return render(request, 'events.html')

def emergency_contact_view(request):
    return render(request, 'emergency_contact.html')

def suggestion_view(request):
    return render(request, 'suggestion.html')
