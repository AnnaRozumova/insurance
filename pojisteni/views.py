from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from pojisteni.forms import PojistenceForm, PojisteniForm, UzivatelForm, LoginForm
from pojisteni.models import Pojistence, Uzivatel

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
    
class UzivatelViewRegister(generic.edit.CreateView):
    form_class = UzivatelForm
    model = Uzivatel
    template_name = 'pojisteni/user_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit = False)
            password = form.cleaned_data['password']
            uzivatel.set_password(password)
            uzivatel.save()
            login(request, uzivatel)
            return redirect('about')
        
        return render(request, self.template_name, {'form':form})
    

class UzivatelViewLogin(generic.edit.CreateView):
    form_class = LoginForm
    template_name = 'pojisteni/user_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect('about')
        return render(request, self.template_name, {'form':form})
    
def logout_user(request):
    logout(request)
    return redirect(reverse('login'))