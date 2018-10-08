from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import OfferCategory, Offer, UserFavorite
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
        offerDetail.click_nums += 1
        offerDetail.save()
        return render(request, "offerDetail.html", {'offerDetail': offerDetail})


class AddFavView(View):
    def post(self, request):

        fav_offer_id = request.POST.get('fav_offer_id', 0)

        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(
            user=request, fav_offer_id=int(fav_offer_id))

        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"seccess","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if fint(av_offer_id) > 0:
                user_fav.fav_offer_id = int(fav_offer_id)
                user_fav.save()
                return HttpResponse('{"status":"seccess","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')
