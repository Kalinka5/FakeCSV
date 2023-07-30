from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CSV_converter.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'CSV_converter.views.handler404'
handler500 = 'CSV_converter.views.handler500'
handler403 = 'CSV_converter.views.handler403'
handler400 = 'CSV_converter.views.handler400'
