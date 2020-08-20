#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Filip Górczyński'
SITENAME = 'Yet Another Developer Blog'
SITEURL = ''

PATH = 'content'

THEME = '/home/filip/src/Vendors/pelican-themes/pelican-blue'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://www.seyiobaweya.tech/articles/2020-01-20/personal-website-setup/
STATIC_PATHS = [
    'images', 'content', 'featured', 'logos' 'pdfs', 'static', 'zipfiles'
]

PLUGIN_PATHS = ['/home/filip/src/Vendors/pelican-plugins']
PLUGINS = [
    'pelican_gist', 'pelican_youtube',
]