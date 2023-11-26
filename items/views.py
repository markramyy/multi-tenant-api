from django.shortcuts import render, redirect

from .models import Item

# Create your views here.
def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def item_detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'items/item_detail.html', {'item': item})

def item_create(request, name, description, price):
    if request.POST:
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Item.objects.create(name=name, description=description, price=price)
        return redirect('item_list')

