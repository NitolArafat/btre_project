
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


#from django.conf.urls import  url, include

urlpatterns = [
    path('',include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('realtors/', include('realtors.urls')),
    path('accounts/', include('accounts.urls')),
    path('',include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
