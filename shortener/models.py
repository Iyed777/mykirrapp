from django.db import models
from django.conf import settings

# Create your models here.
from .utils import create_generator

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_generator()
        super(KirrURL, self).save(*args, **kwargs)


    def __str__(self):
        return(self.url)
