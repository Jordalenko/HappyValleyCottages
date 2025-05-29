from django.shortcuts import render
from django.views import generic
from .models import Cottage

# Create your views here.


class CottageList(generic.ListView):
    # Retrieves Cottage objects from database.
    queryset = Cottage.objects.all()
    # Number of cottages to display per page.
    paginate_by = 2  
    template_name = "cottage_list.html"
    # Allows for loops in template.
    context_object_name = 'cottages'
