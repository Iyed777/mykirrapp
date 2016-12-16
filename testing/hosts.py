from django.conf import settings
from django_hosts import patterns, host

URLConf = getattr(settings, "ROOT_URLCONF", "")

host_patterns = patterns('',
    host(r'www', URLConf, name='www'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
)
