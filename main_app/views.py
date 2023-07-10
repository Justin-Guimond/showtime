from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Showing

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def showings_index(request):
    # showings = Showing.objects.all()
    showings = Showing.objects.filter(user=request.user)
    return render(request, 'showings/index.html', {
        'showings' : showings
    })

def showings_detail(request, showing_id):
    showing = Showing.objects.get(id=showing_id)
    return render(request, 'showings/detail.html', {
        'showing' : showing
    })

class ShowingCreate(CreateView):
    model = Showing
    fields = ['address', 'preferred_time', 'other_availability', 'status', 'notes']

    def form_valid(self, form):
        # self.request.user is the logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ShowingUpdate(UpdateView):
    model = Showing
    fields = ['address', 'preferred_time', 'other_availability', 'status', 'notes']

class ShowingDelete(DeleteView):
    model = Showing
    success_url = '/showings'    