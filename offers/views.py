from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import View
from .models import OfferCategory
# Create your views here.


# def index(request):
# return HttpResponse("welcome to tfg!!!")
# return render(request, 'index.html')

# offers = Offer.objects.all()
# return render(request, 'index.html', {'offers': offers})
# offerCategories = OfferCategory.objects.all().order_by("-count")
# return render(request, 'index.html', {'offerCategories': offerCategories})

class OfferListView(View):
    def get(self, request):
        
        return render(request, "offerList.html", {})
