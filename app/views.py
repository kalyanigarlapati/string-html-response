from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third(request):
    return HttpResponse('kalyani')
def fourth(request):
    return HttpResponse('kalyani g')
def fifth(request):
    return render(request,'kala.html')
