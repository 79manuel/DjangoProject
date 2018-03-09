from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {
        'insert': 'Random text injected in here'
    }

    return render(request, 'manuelapp/index.html', context=my_dict)