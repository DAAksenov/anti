from django.urls import path
from . import views
from vyvod import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ... другие url паттерны ...
    path('load/', views.load_file, name='load_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
