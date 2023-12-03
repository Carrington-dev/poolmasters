from django.contrib import admin
from django.urls import path, include
from config.sitemaps import StaticHomeSitemap, StaticPagesSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticHomeSitemap,
    'static_other': StaticPagesSitemap,
}

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls')),
    path('contact', include('applications.book.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
