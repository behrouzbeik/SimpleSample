from rest_framework import serializers
import requests
from .models import *



class packSerializer(serializers.ModelSerializer):
    senderWeather = serializers.SerializerMethodField('getSenderWeather')
    receiverWeather = serializers.SerializerMethodField('getReceiverWeather')
    
    class Meta:
        model = Pack
        fields = [
            'trackingNumber',
            'carrier',
            'senderStreet',
            'senderRegionalCode',
            'senderCity',
            'senderWeather',
            'senderCountry',
            'receiverStreet',
            'receiverRegionalCode',
            'receiverCity',
            'receiverWeather',
            'receiverCountry',
            'article',
            'quantity',
            'price',
            'sku',
            'status'
        ]

    def getSenderWeather(self, obj):
        url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid=adadee0b7012d40ea31aeae8c0482fa7'.format(obj.senderCity)
        senderWeather = requests.get(url)
        return senderWeather.json()
    
    def getReceiverWeather(self, obj):
        url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid=adadee0b7012d40ea31aeae8c0482fa7'.format(obj.receiverCity)
        receiverWeather = requests.get(url)
        return receiverWeather.json()