from django.shortcuts import render
from django.http import HttpResponse
from manuelapp.models import AccessRecord, Topic, Webpage
from . import forms
# Create your views here.


def index_models(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': webpages_list,
    }

    return render(request, 'manuelapp/index_models.html', context=date_dict)


def index_forms(request):
    return render(request, 'manuelapp/index_forms.html')


def ManuelForm(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation Success')
            print('Name :' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'manuelapp/form.html', {'form': form})

