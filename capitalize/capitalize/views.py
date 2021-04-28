#Created by Ujjawal
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,'index.html') 

def removepunc(request):
    #Get the text
    djtext = request.GET.get('text','default')
    print (djtext)
    #Analyze the text
    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalize First")
    
def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremover(request):    
    return HttpResponse("Space Remover <a href='/'>back</a>"    )

def charcount(request):
    return HttpResponse("Char Count")