from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('download/', include('download.urls')),
    path('test/', include('vyvod.urls'))
]
