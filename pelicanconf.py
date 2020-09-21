#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Filip Górczyński'
SITENAME = 'Yet Another Developer Blog'
SITEURL = 'https://blog.filipgorczynski.me'

PATH = 'content'
THEME = 'theme'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = '/{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

CSS_FILE = 'main.css'
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://www.seyiobaweya.tech/articles/2020-01-20/personal-website-setup/
# STATIC_PATHS = [
#     'images', 'content', 'featured', 'logos' 'pdfs', 'static', 'zipfiles'
# ]

PLUGIN_PATHS = ['/home/filip/src/Vendors/pelican-plugins']
PLUGINS = [
    'pelican_gist', 'pelican_youtube',
]