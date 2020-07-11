from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from tutorial.models import Chapter
#static sitemapp
class postsite(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home','about']
    def location(self, item):
         return reverse(item)    

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
 
    def items(self):
        return Chapter.objects.filter(slug__isnull=False)
 
    # def lastmod(self, obj):
    #     return obj.updated_on


        

#     def location(self, item):
#         return reverse(item)


# dynamic sitemap
# class Chapter(Sitemap):
#     changefreq = "daily"
#     priority = 0.7

#     def items(self):
#         return Chapter.objects.all()

#     def location(self, obj):
#         return obj.full_path

#     def lastmod(self, obj):
#         return obj.date_modified