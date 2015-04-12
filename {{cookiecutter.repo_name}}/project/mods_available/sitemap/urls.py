# -*- coding: utf-8 -*-
"""
Here we bind Sitemap containers for each available apps and ressources

This default config is made to support DjangoCMS, Zinnia, Porticus, staticpages 
and other apps.

By default only DjangoCMS is enabled, uncomment the others or add new app 
ressources for your needs (see the Django sitemap documentation for more details)
"""
from django.conf import settings
from django.core.urlresolvers import reverse

sitemaps = {}

"""
For DjangoCMS
"""
from cms.sitemaps import CMSSitemap
sitemaps['cmspages'] = CMSSitemap


"""
For Zinnia

Commonly, you won't enable tags and authors sitemap
"""
##from zinnia.sitemaps import TagSitemap
#from zinnia.sitemaps import EntrySitemap
#from zinnia.sitemaps import CategorySitemap
##from zinnia.sitemaps import AuthorSitemap

#sitemaps['blog'] = EntrySitemap
#sitemaps['categories'] = CategorySitemap
##sitemaps['tags'] = TagSitemap
##sitemaps['authors'] = AuthorSitemap


"""
For Contact forms
"""
#from project.contact_form.sitemaps import ContactFormEntryBase, ContactFormSitemapBase

#class ContactFormEntry(ContactFormEntryBase):
    #"""Booking form entry for Contact forms sitemap"""
    #url_name = 'contact_form'

#class ContactFormSitemap(ContactFormSitemapBase):
    #"""Contact forms sitemap"""
    #contact_forms = [ContactFormEntry]

#sitemaps['contact'] = ContactFormSitemap


"""
For Porticus objects
"""
#from porticus.sitemaps import PorticusGallerySitemap, PorticusAlbumSitemap, PorticusRessourceSitemap

##sitemaps['galleries'] = PorticusGallerySitemap
#sitemaps['albums'] = PorticusAlbumSitemap
## WARNING: This can make a huge ressource list
##sitemaps['ressources'] = PorticusRessourceSitemap


"""
For Static pages (like prototypes)

Be careful TO NOT ENABLE IN PRODUCTION some integration stuff like page prototypes
"""
#from staticpages.sitemaps import StaticPageSitemapAuto

#class PrototypesSitemap(StaticPageSitemapAuto):
    #"""Prototypes sitemap"""
    #pages_map = settings.STATICPAGES_PROTOTYPES

#sitemaps['prototypes'] = PrototypesSitemap


if sitemaps:
    # Full sitemap
    urlpatterns += patterns('django.contrib.sitemaps.views',
        url(r'^sitemap\.xml$', 'sitemap', {'sitemaps': sitemaps}),
        ## Use sitemap framework to build a JSON map of all resssources
        #url(r'^sitemap\.json$', 'sitemap', {'sitemaps': sitemaps, 'template_name': 'sitemap.json', 'content_type': 'application/json; charset=utf-8'}),
    ) + urlpatterns

    ## Sitemap divised into an index + sections
    #urlpatterns += patterns('django.contrib.sitemaps.views',
        #url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
        #url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
    #) + urlpatterns
