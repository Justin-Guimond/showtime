from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('showings/', views.showings_index, name='index'),
    path('showings/<int:showing_id>/', views.showings_detail, name='detail'),
    path('showings/create/', views.ShowingCreate.as_view(), name='showings_create'),
    path('showings/<int:pk>/update/', views.ShowingUpdate.as_view(), name='showings_update'),
    path('showings/<int:pk>/delete/', views.ShowingDelete.as_view(), name='showings_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]