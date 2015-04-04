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
                       url(r'^client/', views.client, name='Client'),
                       url(r'^login/', views.login, name='Login'),
                       url(r'^pricechart/', views.price_chart, name='Price Chart'),
                       url(r'^depthchart/', views.depth_chart, name='Depth Chart'),
                       url(r'^orderbook/', views.order_book, name='Order Book'),
)
