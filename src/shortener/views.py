from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Shorten_URL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent
# Create your views here.

def home_view(request):

    form = SubmitUrlForm(request.POST)
    context = {
        "title" : "Submit URL",
        "form" : form
    }
    template = "shortener/home.html"

    if form.is_valid():
        new_url = form.cleaned_data.get("url")
        obj, created = Shorten_URL.objects.get_or_create(url=new_url)
        context = {
            "object":obj,
            "created":created,
        }
        if created:
            template = "shortener/success.html"
        else:
            template = "shortener/already-exists.html"

    return render(request, template, context)


def shorten_url_view(request, shorturl=None, *args, **kwargs):

    qs = Shorten_URL.objects.all()
    if not qs.exists():
          raise Http404
    obj = qs.first()
    return HttpResponseRedirect(obj.url)
