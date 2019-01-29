from django.conf.urls import url

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('apps.core.urls')),
    url(r'administracion/', include('apps.administracion.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
