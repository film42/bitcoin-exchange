from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Order, Account, User, Trade, Exchange
from models import TradeTypes, SideTypes, CurrencyTypes, FilledStatusTypes
from rest_framework import viewsets
from serializers import OrderSerializer, TradeSerializer, ExchangeSerializer, AccountSerializer
import requests
import json

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


def add_order(request):
    [user] = User.objects.filter(username="demo")

    form = json.load(request.body)

    if form["side"] == "sell":
        order = Order(order_type=SideTypes.SELL, user=user, amount=form["amount"])
    else:
        order = Order(order_type=SideTypes.BUY, user=user, amount=form["amount"])

    if form["order_type"] == "limit":
        order.order_type = TradeTypes.LIMIT
        order.limit = float(form["limit"])
    else:
        order.order_type = TradeTypes.MARKET
        order.limit = 0.0

    if form["from_currency"] == "BTC":
        order.from_currency = CurrencyTypes.BTC
        order.to_currency = CurrencyTypes.USD
    else:
        order.from_currency = CurrencyTypes.USD
        order.to_currency = CurrencyTypes.BTC

    order.save()

    # Doesn't work for market orders
    # [account] = Account.objects.filter(currency_type=order.from_currency)
    # account.balance = account.balance - order.limit
    # account.save()

    order_json = {
        "orderType": form["side"],
        "orderQuantity": order.amount,
        "orderId": str(order.guid),
        "accountId": str(user.guid)
    }

    if order.order_type == TradeTypes.LIMIT:
        order_json["orderThreshold"] = order.limit

    requests.post("https://darkpool.herokuapp.com/orders/add", data=json.dumps(order_json))

    return HttpResponse("{}")


def open_orders(request):
    template = loader.get_template('exchange/open-orders.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def order_book(request):
    template = loader.get_template('exchange/order-book.html')
    buy_orders, sell_orders = get_orders()
    # sort the orders so that the spread is in the middle
    buy_orders = sorted(buy_orders, key=lambda order: order[1])
    sell_orders = sorted(sell_orders, key=lambda order: order[1], reverse=True)
    # calculate the spread
    spread = min(order[1] for order in sell_orders) - max(order[1] for order in buy_orders)
    context = RequestContext(request, { 'buy_orders': buy_orders, 'sell_orders': sell_orders, 'spread': spread })
    return HttpResponse(template.render(context))


def get_orders():
    buys = []
    sells = []
    json = requests.get('https://darkpool.herokuapp.com/snapshot').json()
    for buy in json['buyBook']:
      buys.append([buy['threshold'], buy['quantity']])
    for sell in json['sellBook']:
      sells.append([sell['threshold'], sell['quantity']])
    # for now we just need it to work (we should fail later if no data is returned)
    if not sells:
        sells = [[0.0, 0.0]]
    if not buys:
        buys = [[0.0, 0.0]]
    return buys, sells


def get_depth_chart():
    buys, sells = get_orders()
    return str([buys, sells])


def get_price_chart():
    trades = []
    trades_json = requests.get('https://darkpool.herokuapp.com/trades?limit=250').json()
    cur_date = len(trades_json)
    for trade in trades_json:
      trades.append([cur_date, trade['price']])
      cur_date -= 1
    return str(trades)
