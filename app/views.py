from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy


class home(TemplateView):
    template_name='app/home.html'


class School_list(ListView):
    model=School
    template_name='app/school_list.html'
    context_object_name='schools'
    

class School_detail(DetailView):
    model=School
    context_object_name='sclobj'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
    context_object_name='sclobject'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobject'
    success_url=reverse_lazy('School_list')
