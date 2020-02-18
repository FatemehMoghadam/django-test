from django.urls import path

from . import views

from .views import (
    CarListView,
    CarDetailView,
    CarDeleteView,
    CarCreateView
 )
 
app_name = 'thecut'

urlpatterns = [
    path('', views.index, name='index'),
    path('listView/', CarListView.as_view(), name = 'car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name = 'car_detail'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name = 'car_delete'),
    path('create/', CarCreateView.as_view(), name = 'car_create'),
]