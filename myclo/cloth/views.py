from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def clothes(request):
    return render(request, 'clothes.html')