
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    variables = {}
    return render(request=request, template_name='index.html', context=variables)



# Create your views here.
