from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shortener.models import  Shorten_URL
from shortener.api.serializers import ShortenUrlSerializer

@api_view(['GET'])
def get_short_url_api(request):
    base_url = 'http://127.0.0.1:8000/'
    try:
        short_url = Shorten_URL.objects.all()
    except Shorten_URL.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    result = []
    for i in short_url:
        serializer = ShortenUrlSerializer(i)
        res_dict = serializer.data
        res_dict['shorturl'] = base_url+res_dict['shorturl']
        result.append(res_dict)

    return Response(result)

@api_view(['POST'])
def create_short_url_api(request, raw_url):
    short_url = Shorten_URL.objects.get_or_create(url=raw_url)
    if short_url:
        serializer = ShortenUrlSerializer(short_url)
        return Response(serializer.data)
    else:
        return Response(status.HTTP_400_BAD_REQUEST)


