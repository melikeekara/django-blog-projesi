from django.contrib import admin
from django.urls import path, include
from bloge.views import iletisim
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('bloge.urls')),
    path('', include('bloge.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)