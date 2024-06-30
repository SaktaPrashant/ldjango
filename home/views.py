from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the data")

def paths(request):
    context = {
        'heading' : "Django tutorial 1"
        'context'  "This is a way of using Django"
    }
    return HttpResponse("This is the data for the paths")