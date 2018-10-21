from .models import OfferCategory, Offer
import xadmin
from xadmin import views

# change themes
# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True

# import_excel = True

# change global setting


class GlobalSettings(object):
    site_title = "TFG.TOKYO 管理シスタム"
    site_footer = "tfg.tokyo"
    menu_style = "accordion"


class OfferCategoryAdmin(object):
    list_display = ('name', 'count')
    ordering = ['-count']


class OffersAdmin(object):
    list_display = ['title', 'create_date', 'create_by',
                    'last_modified_date', 'last_modified_by', 'isActive', 'click_nums', 'fav_nums', 'apply_nums']
    search_fields = ['title', 'create_by', 'click_nums', 'fav_nums', 'apply_nums']
    list_filter = ['title', 'create_date', 'create_by',
                   'last_modified_date', 'last_modified_by', 'click_nums', 'fav_nums', 'apply_nums']
    readonly_fields = ('click_nums', 'fav_nums', 'apply_nums')
    model_icon = 'fa fa-book'
    ordering = ['-pub_time']
    exclude = ['create_by', 'last_modified_by']

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        # obj实际是一个course对象
        obj = self.new_obj
        request = self.request
        obj.create_by = str(request.user)
        obj.last_modified_by = str(request.user)
        # 如果这里不保存，新增课程，统计的课程数会少一个
        obj.save()
        # 确定课程的课程机构存在。
        if obj.offerCategory is not None:
            #找到添加的课程的课程机构
            offerCategory = obj.offerCategory
            #课程机构的课程数量等于添加课程后的数量
            offerCategory.count = Offer.objects.filter(offerCategory=offerCategory).count()
            offerCategory.save()


# change themes
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Offer, OffersAdmin)
xadmin.site.register(OfferCategory, OfferCategoryAdmin)
