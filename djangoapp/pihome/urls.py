from django.urls import path
from pihome.views import index
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pihome'

urlpatterns = [
    path('', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

