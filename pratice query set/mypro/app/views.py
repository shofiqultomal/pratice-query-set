from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Members

# Create your views here.
def home(request):
    mymembers=Members.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))
