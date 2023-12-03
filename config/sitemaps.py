from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse




class StaticHomeSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)
    
class StaticPagesSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['about', 'services', 'contact', 'testimony', 'portfolio']

    def location(self, item):
        return reverse(item)