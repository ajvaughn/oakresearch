from django.shortcuts import render_to_response
from inventory_tracker.models import Item


def index(request):
    items_list = Item.objects.all()

    return render_to_response('inventory_tracker/index.html',
        {'items_list': items_list})


def inventory_detail(request, inventory_id):
    pass
