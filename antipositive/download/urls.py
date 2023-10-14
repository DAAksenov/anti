from django.urls import path
from . import views
from download import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ... другие url паттерны ...
    path('upload/', views.upload_file, name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
