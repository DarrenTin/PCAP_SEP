from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Line, Station
# Create your views here.

# class View1(TemplateView):  #class based view
#     template_name = 'template1.html'

# def view1(request): #function based view
#     return render(request, "template1.html")

def view1(request): #function based view
    stations = Station.objects.all()
    return render(request, "template1.html", {"stations" : stations})