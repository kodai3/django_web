from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,
                                 TemplateView,
                                 ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView)
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

# Create your views here.
class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchooldetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = (
        'name', 'principal'
    )
    model = models.School

class SchoolDeleteVew(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
