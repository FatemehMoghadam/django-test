from django.shortcuts import render, redirect

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView
)

from .models import Car, Manufacturer
from .forms import CarForm, ManufacturerForm


class CarListView(ListView):
    template_name = 'thecut/car_list.html'
    queryset = Car.objects.all()

class CarDetailView(DetailView):
    template_name = 'thecut/car_detail.html'
    queryset = Car.objects.all()

class CarDeleteView(DeleteView):
    template_name = 'thecut/car_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        print("ey baba")
        print(id_)
        return get_object_or_404(Car, pk=id_)

    def get_success_url(self):
        return reverse('thecut:car_list')

class CarCreateView(CreateView):
    template_name = 'thecut/car_create.html'
    form_class = CarForm
    queryset = Car.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

@csrf_exempt
def index(request):
    return render(request, 'thecut/base.html', {})
