from django.shortcuts import render
from django.views import generic
from .models import Cottage

# Create your views here.


class CottageList(generic.ListView):
    queryset = Cottage.objects.all()
    template_name = "cottage_list.html"
