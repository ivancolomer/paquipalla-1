from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic

from .models import Company, Envelope

# Create your views here.

class CompanyListView(generic.ListView):
    model = Company

class CompanyDetailView(generic.DetailView):
    model = Company
