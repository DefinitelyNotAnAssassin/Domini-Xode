from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return ['index', 'articles', 'events', 'yearlist' , 'testimonials']

    def location(self, item):
        return reverse(item)