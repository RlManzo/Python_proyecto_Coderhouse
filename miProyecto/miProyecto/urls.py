from django.contrib import admin
from django.urls import path, include
from AppCoder.views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path("", inicio)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 