from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from LandingPage import views
from LandingPage.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [

    path('', views.index, name = 'index'),
    path('tools/coding_ai', views.coding_ai, name = 'coding ai'),
    path('tools/prettier/html', views.html_prettier, name = 'html prettier'),
    path('upload_file', views.upload_file, name = 'upload file'),
    path('robots.txt', TemplateView.as_view(template_name="LandingPage/robots.txt", content_type="text/plain"), name="robots_file"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

]