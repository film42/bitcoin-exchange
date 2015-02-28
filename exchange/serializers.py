from rest_framework import serializers
from exchange.models import Order, Trade, Exchange, Account


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account


