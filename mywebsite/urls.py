
from django.contrib import admin
from django.urls import path ,include
from  tutorial import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from tutorial.sitemap import StaticViewSitemap,postsite

sitemaps = {
    'post' : postsite,
    'static': StaticViewSitemap,
}

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('tutorial.urls')),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
     path('About', views.about , name='about'),
     path('Sitemap', views.sitemap , name='sitemap'),
     path('ckeditor', include('ckeditor_uploader.urls')),
     path('robots.txt', include('robots.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

