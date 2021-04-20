#Created by Ujjawal
from django.http import HttpResponse
def gfg(request):
    s='''<a href="https://practice.geeksforgeeks.org/explore/?page=1">Geeks for Geeks</a>
        </br>
        <a href="https://www.facebook.com">Facebook</a>
        </br>
        <a href="https://www.youtube.com">Youtube</a>
        </br>
        <a href="https://www.codewithharry.com">Code with Harry</a>
        </br>
        <a href="https://www.abc.com">ABC</a>'''
    return HttpResponse(s)
