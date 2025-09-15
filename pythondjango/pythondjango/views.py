# hello world
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render 
def home(request):
    # return HttpResponse('hello world')
    return render(request, 'index.html')

def about(request):
    data = {
        "message": "Hello, this is my first API response!",
        "status": "success"
    }
    return JsonResponse(data)


def contact(request):
    return HttpResponse('contact')