from django.shortcuts import render

# Create your views here.
from . import forms
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm



class registerPage(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name="accounts/registration.html"

    

    
    

