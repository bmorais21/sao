"""URLs do projeto"""

from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

urlpatterns = i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('saoapp.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
