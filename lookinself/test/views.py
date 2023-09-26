from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def test(request):
    template = loader.get_template('html/pages/test.html')
    return HttpResponse(template.render({"title": "test page"}, request))

# Create your views here.
