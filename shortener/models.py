from django.db import models
from django.conf import settings

from django_hosts.resolvers import reverse

# Create your models here.
from .utils import create_generator
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs


    def refresh_shortcode(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('id')[:items]
        new_code = 0
        for q in qs:
            q.shortcode = create_generator(q)
            print(q.id)
            q.save()
            new_code += 1

        return "New code made :{0}".format(new_code)



class KirrURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_generator(self)
        super(KirrURL, self).save(*args, **kwargs)


    def __str__(self):
        return(self.url)

    def get_short_url(self):
        return reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme="http")
