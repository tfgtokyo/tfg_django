from .models import OfferCategory, Offer
import xadmin
from xadmin import views

# change themes
# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True


# change global setting
class GlobalSettings(object):
    site_title = "TFG.TOKYO 管理シスタム"
    site_footer = "tfg.tokyo"
    menu_style = "accordion"


class OfferCategoryAdmin(object):
    list_display = ('name', 'count')


class OffersAdmin(object):
    list_display = ['title', 'create_date', 'create_by',
                    'last_modified_date', 'last_modified_by']
    search_fields = ['title', 'create_by']
    list_filter = ['title', 'create_date', 'create_by',
                   'last_modified_date', 'last_modified_by']


# change themes
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Offer, OffersAdmin)
xadmin.site.register(OfferCategory, OfferCategoryAdmin)
