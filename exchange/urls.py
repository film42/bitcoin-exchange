from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from exchange import views

admin.autodiscover()

router = DefaultRouter(trailing_slash=False)
router.register(r'orders', views.OrderViewSet)
router.register(r'trades', views.TradeViewSet)
router.register(r'exchanges', views.ExchangeViewSet)
router.register(r'accounts', views.AccountViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^home/', views.home, name='Home'),
)
