from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showings/', views.showings_index, name='index'),
    path('showings/<int:showing_id>/', views.showings_detail, name='detail'),
    path('showings/create/', views.ShowingCreate.as_view(), name='showings_create'),
]