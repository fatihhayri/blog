#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = 'Fatih'
SITENAME = u'Fatih Hayrioğlu\'nun not defteri'
SITESUBTITLE = u'{ CSS, XHTML ve Javascript }'
SITEURL = 'http://www.fatihhayrioglu.com'

# Where to output the generated files.
OUTPUT_PATH = 'html/'

# path to look at for input files.
PATH = "source"

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = 'tr'
LOCALE = ('tr_TR',)
DATE_FORMAT = {
   'tr': '%d %b %Y'
}
THEME = 'theme'

DISPLAY_PAGES_ON_MENU = False
#DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

MD_EXTENSIONS = ['codehilite', 'extra']
STATIC_PATHS = ['dokumanlar', 'images',]
MENUITEMS = [('Anasayfa', '/'),
             (u'Hakkımda', '/hakkimda/'),
             ('CSS Dersleri', '/css-dersleri/'),
             ('Kitap', '/kitap/')]
# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('@fatihhayri', 'http://twitter.com/fatihhayri'),)

PLUGINS=['pelican.plugins.related_posts',]

DEFAULT_PAGINATION = 10
TWITTER_USERNAME = "fatihhayri"
DISQUS_SITENAME = "fatihhayri"
GOOGLE_ANALYTICS = "UA-785768-1"
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon.ico', 'favicon.ico'))

FEED_MAX_ITEMS = 10
