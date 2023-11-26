from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import Item

# Create your views here.
class ItemListView(generic.ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'items/item_detail.html'
    context_object_name = 'item'


class ItemCreateView(generic.CreateView):
    model = Item
    template_name = 'items/item_create.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('items:item_list')


class ItemUpdateView(generic.UpdateView):
    model = Item
    template_name = 'items/item_update.html'
    fields = ['description', 'price']
    success_url = reverse_lazy('items:item_list')


class ItemDeleteView(generic.DeleteView):
    model = Item
    template_name = 'items/item_delete.html'
    success_url = reverse_lazy('items:item_list')

