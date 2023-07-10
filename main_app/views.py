from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Showing

# Create your views here.
def home(request):
    return render(request, 'home.html')

def showings_index(request):
    showing = Showing.objects.all()
    return render(request, 'showings/index.html', {
        'showing' : showing
    })
    