from django.shortcuts import render, HttpResponse
from .models import membersModel

# Create your views here.
def index_view(request):
    querySet = membersModel.objects.all()
    print(querySet)
    for member in querySet:
        print(member.first_name)
    return render(request, 'index.html')