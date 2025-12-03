"""
URL configuration for personal_tech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from . import views
from .sitemaps import StaticViewSitemap
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('empresa/nosotros/', views.about, name='about'),
    path('empresa/historia/', views.history, name='history'),
    path('empresa/equipo/', views.team, name='team'),
    # Service Pages
    path('servicios/soporte-tecnico/', views.service_support, name='service_support'),
    path('servicios/desarrollo-software/', views.service_development, name='service_development'),
    path('servicios/redes-comunicaciones/', views.service_networks, name='service_networks'),
    path('servicios/soluciones-cloud/', views.service_cloud, name='service_cloud'),
    path('servicios/ciberseguridad/', views.service_security, name='service_security'),
    path('servicios/consultoria-ti/', views.service_consulting, name='service_consulting'),
    path('services/', include('services.urls')),
    path('inventory/', include('inventory.urls')),
    path('quotes/', include('quotes.urls')),
    path('reports/', include('reports.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
