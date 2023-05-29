from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from pojisteni.forms import PojistenceForm, PojisteniForm
from pojisteni.models import Pojistence

# Create your views here.

def pojistence(request):
    return render(request, 'pojisteni/pojistence.html')

def pojisteni(request):
    return render(request, 'pojisteni/pojisteni.html')

def about(request):
    return render(request, 'pojisteni/about.html')

class CreatePojistence(generic.edit.CreateView):

    form_class = PojistenceForm
    template_name = 'pojisteni/create_pojistence.html'

    def get(self, request):
        form_1 = self.form_class(None)
        return render(request, self.template_name, {'form_1':form_1})
    
    def post(self, request):
        form_1 = self.form_class(request.POST)
        if form_1.is_valid():
            form_1.save(commit=True)
        return render(request, self.template_name, {'form_1':form_1})
    

class CreatePojisteni(generic.edit.CreateView):

    form_class = PojisteniForm
    template_name = 'pojisteni/create_pojisteni.html'

    def get(self, request):
        form_2 = self.form_class(None)
        return render(request, self.template_name, {'form_2':form_2})
    
    def post(self, request):
        form_2 = self.form_class(request.POST)
        if form_2.is_valid():
            form_2.save(commit=True)
        return render(request, self.template_name, {'form_2':form_2})


class PojistenceIndex(generic.ListView):

    template_name = 'pojisteni/pojistence.html'
    context_object_name = 'pojistence'

    def get_queryset(self):
        return Pojistence.objects.all().order_by('id_pojistence')