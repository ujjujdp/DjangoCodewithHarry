#Created by Ujjawal
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

