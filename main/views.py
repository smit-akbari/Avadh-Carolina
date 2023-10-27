from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import datetime
from authentication.helpers import require_access_token,decode_jwt_token
from authentication.models import membersModel,memberProfileModel
from .models import services, clubHouseBooking, emergencyContactsModel, eventsModel, galleryModel
import random


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
    email = decode_jwt_token(request.session.get('token'))['email']
    getMember = membersModel.objects.get(email=email)
    getMemberProfile = memberProfileModel.objects.get(member_id_id= getMember.id)

    member_data = {
        'member_id': getMember.id,
        'first_name':getMember.first_name,
        'last_name':getMember.last_name,
        'email':getMember.email,
        'mobile':getMember.mobile,
        'profile': getMemberProfile.profile.url,
        'gender': getMemberProfile.gender
    }
    request.session['member_data'] = member_data

    # Pass the greeting and user_name to the template
    context = {
        'greeting': greeting,
        'member_name': f"{getMember.first_name} {getMember.last_name}"
    }
    return render(request, 'dashboard.html', context)


@require_access_token
def services_view(request):
    services_ = services.objects.all()
    bookings_ = clubHouseBooking.objects.all()

    # Shuffle the services_ list randomly
    shuffled_services = list(services_)
    random.shuffle(shuffled_services)

    # Select the first 6 services from the shuffled list
    services_ = shuffled_services[:6]
    
    context = {
       'services' : services_,
       'bookings' : bookings_
    }
    return render(request, 'services.html', context)

@require_access_token
def addEvent(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        content = request.POST['content']

        member_id = request.session.get('member_data')['member_id']
        # print(event_name, from_date, to_date, content, member_id)

        create_club = clubHouseBooking.objects.create(
            member_id_id=member_id,
            event_name=event_name,
            from_date=from_date,
            to_date=to_date,
            content=content
        )
        create_club.save()
        messages.success(request, f'{event_name} - Event added')
        return redirect('services_view')
    return redirect('services_view')

def delete_event(request, booking_id):
    getBooking = clubHouseBooking.objects.get(id = booking_id)
    getBooking.delete()
    return redirect('services_view')

def gallery_view(request):
    gallery_pic_ = galleryModel.objects.all()
    context = {
        'gallery_pic' : gallery_pic_
    }
    return render(request, 'gallery.html',context)

def events_view(request):
    event_card_ = eventsModel.objects.all()
    context = {
        'event_card' : event_card_
    }
    return render(request, 'events.html' , context)

def emergency_contact_view(request):
    contact_card_ = emergencyContactsModel.objects.all()
    context = {
       'contact_card' : contact_card_ 
    }
    return render(request, 'emergency_contact.html',context)

def suggestion_view(request):
    return render(request, 'suggestion.html')
