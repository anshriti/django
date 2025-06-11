from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo( request):
    #print("Hello world")
    return HttpResponse("Hello this is my first django app")

def country(request):
    context = {
        "country_name" : "Nepal",
        "continent": "Asia",
        "country_code": "+977" 
    }
    return render(request, "country.html", context)

def province(request):
    context = {
        "province_name":"Bagmati",
        "province_code":"800"

    }
    return render(request, "province.html",context)

def trial(request):
    return render(request, "trial.html")
