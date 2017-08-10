from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^', include('event_planner_app.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]