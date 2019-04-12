from django.shortcuts import render
from .models import Item

# Create your views here.
def item_list(request):
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html', {
        'item_list' : qs,
    })

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item' : item,
    })
