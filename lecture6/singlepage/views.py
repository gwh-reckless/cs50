from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

sections = [
    'section1',
    'section2',
    'section3'
]


def index(request):
    return render(request, 'singlepage/index.html')


def section(request, section_id):
    return HttpResponse(sections[section_id-1])
