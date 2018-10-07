from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import View
from .models import OfferCategory, Offer
# Create your views here.


# def index(request):
# return HttpResponse("welcome to tfg!!!")
# return render(request, 'index.html')

# offers = Offer.objects.all()
# return render(request, 'index.html', {'offers': offers})
# offerCategories = OfferCategory.objects.all().order_by("-count")
# return render(request, 'index.html', {'offerCategories': offerCategories})

class CategoryListView(View):
    def get(self, request):
        offerCategories = OfferCategory.objects.all().order_by("-count")
        return render(request, "index.html", {'offerCategories': offerCategories})


class OfferListView(View):
    def get(self, request, category_id):
        category = OfferCategory.objects.get(id=int(category_id))
        offerList = category.offer_set.values(
            'id', 'title', 'pub_time', 'click_nums', 'fav_nums', 'apply_nums').filter(isActive=0).order_by("-pub_time")
        return render(request, "offerList.html", {'offerList': offerList})


class OfferDetailView(View):
    def get(self, request, offer_id):
        offerDetail = Offer.objects.get(id=int(offer_id))
        return render(request, "offerDetail.html", {'offerDetail': offerDetail})
