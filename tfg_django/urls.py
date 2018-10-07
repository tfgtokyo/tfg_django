"""tfg_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import xadmin
# from users.views import login, signup
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from users import views as users_views
from offers.views import CategoryListView, OfferListView, OfferDetailView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    # path('index/', include('offers.urls')),
    # path('offers/', include('offers.urls')),

    path('users/', include('django.contrib.auth.urls')),

    # path('signup/', signup, name="signup"),
    path('signup/', users_views.signup, name='signup'),

    # path('login/', login, name="login")
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'), name='password_change'),

    path('index/', CategoryListView.as_view(), name="index"),

    re_path(r'^offerList/(?P<category_id>\d+)/$',
            OfferListView.as_view(), name="offerList"),

    re_path(r'^offerDetail/(?P<offer_id>\d+)/$',
            OfferDetailView.as_view(), name="offerDetail"),
]
