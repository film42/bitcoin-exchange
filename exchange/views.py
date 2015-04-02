from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import *
from rest_framework import viewsets
from serializers import OrderSerializer, TradeSerializer, ExchangeSerializer, AccountSerializer
import requests

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


def home(request):
    template = loader.get_template('exchange/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def client(request):
    template = loader.get_template('exchange/client-view.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def login(request):
    template = loader.get_template('exchange/login.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def price_chart(request):
    json = get_price_chart()
    return HttpResponse(json)


def depth_chart(request):
    json = get_depth_chart()
    return HttpResponse(json)


def get_depth_chart():
    buys = []
    sells = []
    json = requests.get('https://darkpool.herokuapp.com/snapshot').json()
    for buy in json['buyBook']:
      buys.append([buy['threshold'], buy['quantity']])
    for sell in json['sellOrder']:
      sells.append([sell['threshold'], sell['quantity']])
    return str([buys, sells])
    #return '[[[0,30],[6,15],[11,9],[19,3],[27,0]],[[28,0],[35,3],[42,9],[49,15],[58,30]]]'


def get_price_chart():
    trades = []
    cur_date = 0
    trades_json = requests.get('https://darkpool.herokuapp.com/trades?limit=250').json()
    for trade in trades_json:
      trades.append([cur_date, trade['price']])
      cur_date += 1
    return str(trades)
    #return '[[0,0],[3, 6],[9, 11],[15, 19],[30, 27]]'
