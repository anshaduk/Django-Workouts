from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFunc(req):
    return HttpResponse("Hello this is the test file..!!")

def TestFunc1(req):
    return HttpResponse("This is the second test")

def TestFunc2(req):
    return HttpResponse("This is third test")

def indexFunc(req):
    return render(req,'index.html')

def aboutFunc(req):
    return render(req,'about.html')