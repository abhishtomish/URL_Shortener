import string
import random
from django.conf import settings
# from shortener.models import Shorten_URL

SHORTURL_MIN = getattr(settings, "SHORTURL_MIN", 6)

def code_generator(size=SHORTURL_MIN, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def create_shorturl(instance, size=6):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs = Klass.objects.filter(shorturl=new_code).exists()
    if qs:
        return create_shorturl(size=size)
    return new_code