from django.shortcuts import render, HttpResponse

# Create your views here.
def printText(request):
    return HttpResponse( "ejulu wilson rocks!!")