from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def questions(request):
    template = loader.get_template('html/pages/questions.html')
    return HttpResponse(template.render({"title": "questions page"}, request))

# Create your views here.
