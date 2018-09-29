from django.shortcuts import render
# from django.http import HttpResponse
from .models import OfferCategory
# Create your views here.


def index(request):
    # return HttpResponse("welcome to tfg!!!")
    # return render(request, 'index.html')

    # offers = Offer.objects.all()
    # return render(request, 'index.html', {'offers': offers})
    offerCategories = OfferCategory.objects.all()
    return render(request, 'index.html', {'offerCategories': offerCategories})
