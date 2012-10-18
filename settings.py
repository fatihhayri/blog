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

MENUITEMS = [('Anasayfa', '/'),
             (u'Hakkımda', '/hakkimda/'),
             ('CSS Dersleri', '/css-dersleri/'),
             ('Kitap', '/kitap/')]
# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('@fatihhayri', 'http://twitter.com/fatihhayri'),)
FEED_DOMAIN =  'http://feeds.feedburner.com'
FEED_ATOM = 'fatihhayri'

DEFAULT_PAGINATION = 10

TWITTER_USERNAME = "fatihhayri"
DISQUS_SITENAME = "fatihhayri"
GOOGLE_ANALYTICS = "UA-785768-1"

