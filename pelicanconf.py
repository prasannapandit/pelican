#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Prasanna Pandit'
SITENAME = u'Odds and Ends'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
 #         ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = '/home/pvpandit/blog/pelican-themes/elegant'

LANDING_PAGE_ABOUT = {'title': 'Prasanna Pandit', 'details': 'Occasional blogger. Federer fan. Love non-fiction and lolz. Went to IISc and drank lots of tea.'};

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
