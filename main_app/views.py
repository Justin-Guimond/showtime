from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Showing
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)