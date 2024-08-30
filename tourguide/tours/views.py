from django.shortcuts import render
from django.shortcuts import loader
from django.http import HttpResponse
from .models import Tour
# Create your views here.
def tours(request):
    all_tours = Tour.objects.all().values()
    template = loader.get_template('all_tours.html')
    context = {
        'all_tours': all_tours
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def details(request, id):
    tour = Tour.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'tour': tour,
    }
    return HttpResponse(template.render(context, request))
    