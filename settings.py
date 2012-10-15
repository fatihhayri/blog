#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Fatih'
SITENAME = u'Fatih Hayrioğlu'
SITEURL = 'http://www.fatihhayrioglu.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'tr'
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

DISQUS_SITENAME = "fatihhayri"
GOOGLE_ANALYTICS = "UA-785768-1"
