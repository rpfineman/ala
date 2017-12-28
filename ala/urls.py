#
# URLS (project)
#
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [ url(r'^admin/', admin.site.urls), ]
#
from django.conf.urls import include
urlpatterns += [ url(r'^feeds/', include('feeds.urls')), ]
#
from django.views.generic import RedirectView
urlpatterns += [ url(r'^$', RedirectView.as_view(url='/feeds/', permanent=True)), ]
#
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

