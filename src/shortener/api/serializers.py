from rest_framework import serializers
from shortener.models import Shorten_URL

class ShortenUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Shorten_URL
        fields = ['shorturl', 'updated']