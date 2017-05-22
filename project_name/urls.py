from django.conf.urls import url, include
from django.contrib import admin
from drf_auto_endpoint.router import router
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                       document_root=settings.MEDIA_ROOT)

admin.site.site_header='{{project_name}} Backend'