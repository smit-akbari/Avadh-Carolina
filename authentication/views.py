from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import membersModel
from .helpers import create_jwt_token, require_access_token
from django.http import Http404

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            CHECK_MEMBER = membersModel.objects.get(email=email)
        except membersModel.DoesNotExist:
            messages.error(request, "Member does not exist")
            return render(request, 'login.html')
        else:
            if len(email) != 0 and len(password) != 0 and CHECK_MEMBER:
                if password == CHECK_MEMBER.password:
                    request.session['token'] = create_jwt_token(email)

                    print(request.session.get('token'))
                    messages.success(request, "Now you are logged in")
                    return redirect('dashboard_view')
                else:
                    messages.error(request, "Incorrect Email or Password")
                    return render(request, 'login.html')
    return render(request, 'login.html')

# Create your views here.
def index_view(request):
    querySet = membersModel.objects.all()
    print(querySet)
    for member in querySet:
        print(member.first_name)
    return render(request, 'index.html')