from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('list.urls', namespace='list'))
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    """