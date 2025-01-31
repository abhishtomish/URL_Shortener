from django.db import models
from shortener.models import Shorten_URL

# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, kirrInstance):
        if isinstance(kirrInstance, Shorten_URL):
            obj, created = self.get_or_create(kirr_url=kirrInstance)
            obj.count+=1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    kirr_url    = models.OneToOneField(Shorten_URL, on_delete=models.CASCADE)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)