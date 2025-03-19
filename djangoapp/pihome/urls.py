from django.urls import path
from pihome.views import index, lightRoom
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pihome'

urlpatterns = [
    path('', index, name='index'),
    path('light-room/', lightRoom, name='lightRoom'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

