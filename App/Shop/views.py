from django.shortcuts import render
from .models import Basket, Item


# Create your views here.
def index(request):
    Iter = []
    for i, obj in enumerate(Item.objects.all()):
        Iter.append(i+1)
    context = {
        "Baskets": Basket.objects.all(),
        "Items": Item.objects.all(),
        "ITERATE_ITEMS": Iter

    }

    return render(request, "Shop/Home.html", context)


def Auth(request):
    Iter = []
    for i, obj in enumerate(Item.objects.all()):
        Iter.append(i)
    context = {
        "Baskets": Basket.objects.all(),
        "Items": Item.objects.all(),
        "ITERATE_ITEMS": Iter

    }
    return render(request, "Shop/Authentication.html", context)
