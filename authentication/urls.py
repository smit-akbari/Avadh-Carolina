from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('dashboard/', index_view, name='index_view'),
]