"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.views import IndexView, not_found_view, internal_error_view, forbidden_view, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('', include('apps.user.urls')),
    path('', include('apps.post.urls')),
    path('about/', AboutView.as_view(), name='about')
]
# Manejadores de errores
handler404 = not_found_view
handler500 = internal_error_view
handler403 = forbidden_view
# Los manejadores estan disponibles en cualquier parte de la aplicación,
# por lo que no es necesario importarlos en cada vista.
# o incluso aqui en blog\blog\urls.py

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                            document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root = settings.MEDIA_ROOT)
    
