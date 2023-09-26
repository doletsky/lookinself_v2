from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def sign(request):
    template = loader.get_template('html/pages/sign.html')
    return HttpResponse(template.render({"title": "sign page"}, request))

# Create your views here.
