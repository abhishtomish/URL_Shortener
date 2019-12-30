from django.conf import settings
from django.db import models
from .utils import code_generator, create_shorturl

# Create your models here.

SHORTURL_MAX = getattr(settings, "SHORTURL_MAX", 15)

class ShortenURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortenURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shorturl(self):
        qs = Shorten_URL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.short_url = create_shorturl(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class Shorten_URL(models.Model):
    url         = models.CharField(max_length = 220, )
    shorturl    = models.CharField(max_length = SHORTURL_MAX, unique=True, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    objects     = ShortenURLManager()

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.shorturl is None or self.shorturl == "":
            self.shorturl = create_shorturl(self)
        super(Shorten_URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        return "http://127.0.0.1:8000/{shorturl}".format(shorturl=self.shorturl)
