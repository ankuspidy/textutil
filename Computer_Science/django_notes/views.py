from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html')


def index1(request):
    return render(request, 'index1.html')

def hell(request):
    template = loader.get_template('index1.html')
    context = {"username": "vishal"}
    return HttpResponse(template.render(context))


