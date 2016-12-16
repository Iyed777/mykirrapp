from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views import View
# Create your views here.

from analytics.models import ClickEvent

from .models import KirrURL
from .forms import SubmitURLForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm()
        context = {
            "title": "Submit form",
            "form": the_form
        }
        return render(request, "home.html", context)


    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        template = "home.html"
        context = {
            "title": "Submit form",
            "form": form
        }
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "success.html"
            else:
                template = "exists.html"
        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        """qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()"""
        print(ClickEvent.objects.creare_event(obj))
        return HttpResponseRedirect(obj.url)
