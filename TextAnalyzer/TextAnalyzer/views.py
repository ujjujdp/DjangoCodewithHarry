#Created by Ujjawal
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    params = {'name':'Ujjawal Dewangan','place':'Jagdalpur'}
    return render(request,'index.html',params) 

def analyzetext(request):
    #Get the Text
    djtext = request.POST.get('text','default')
    #Checkbox   
    rempun= request.POST.get('removepunc','off')
    cap = request.POST.get('cap','off')
    nlr = request.POST.get('nlr','off')
    sr = request.POST.get('sr','off')
    cc = request.POST.get('cc','off')
    print (djtext)  
    analyzed=djtext
    #Remove Punctuaions
    if rempun == "on":
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed=analyzed+char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyzetext.html',params) 
         
    #Capitalize
    if cap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capitalize','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyzetext.html',params) 

    #NewLineRemover
    if nlr == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!= '\r': 
                analyzed=analyzed+char
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyzetext.html',params)
        #  
    #Space Remover
    if sr == "on":
        analyzed = ""
        flag=0
        for char in djtext:
            if char == ' ':
                flag=1
                continue    
            if flag == 1:
                analyzed=analyzed+' '+char
            else:
                analyzed=analyzed+char
            flag=0
        params = {'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyzetext.html',params) 

    #Character Counter
    if cc == "on":
        count=0
        for char in djtext: 
            count = count +1
        te = analyzed + "\n\nCount = " + str(count)
        params = {'purpose':'Character Count','analyzed_text':te}
        #return render(request,'analyzetext.html',params) 

    #Nothing is Selected
    if(rempun=="off" and cap=="off" and sr=="off" and nlr=="off" and cc=="off"):
        return HttpResponse("Nothing is selected")
    return render(request,'analyzetext.html',params) 
# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text','default')
#     print (djtext)
#     #Analyze the text
#     params = {'name':'Ujjawal Dewangan','place':'Jagdalpur'}
#     return render(request,'removepunc.html',params) 
#     #return HttpResponse("Remove Punc")

# def capfirst(request):
#     params = {'name':'Ujjawal Dewangan','place':'Jagdalpur'}
#     return render(request,'capfirst.html',params) 
#     #return HttpResponse("Capitalize First")
    
# def newlineremove(request):
#     params = {'name':'Ujjawal Dewangan','place':'Jagdalpur'}
#     return render(request,'newlineremover.html',params) 
#     #return HttpResponse("New Line Remove")

# def spaceremover(request):    
#     params = {'name':'Ujjawal Dewangan','place':'Jagdalpur'}
#     return render(request,'spaceremover.html',params)
#     #return HttpResponse("Space Remover <a href='/'>back</a>"    )


# def charcount(request):
#     params = {'name':'Ujjawal Dewangan','place':'Jagdalpur'}
#     return render(request,'charcount.html',params) 
#     #return HttpResponse("Char Count")