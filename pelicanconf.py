#!/usr/bin/env python
# https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example

AUTHOR = 'Filip Górczyński'
SITENAME = 'Filip Górczyński'
SITETITLE = "Filip Górczyński"
SITEURL = 'http://127.0.0.1:8004/'
SITESUBTITLE = "Jack of all trades; Master of one."
SITEDESCRIPTION = "Jack of all trades; Master of one."
SITELOGO = SITEURL + "img/profile.png"
FAVICON = SITEURL + "img/favicon.ico"
BROWSER_COLOR = "#efefef"
ROBOTS = "index, follow"
# PATH = 'content'
THEME = '/home/filip/src/Vendors/pelican-themes/Flex'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'pl'
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}
# CUSTOM_CSS = "static/custom.css"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None # "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
COPYRIGHT_YEAR = 2020
PAGE_URL = '/{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = '/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
HOME_HIDE_TAGS = True
MAIN_MENU = True

# ADD_THIS_ID = "ra-77hh6723hhjd"
# DISQUS_SITENAME = "yoursite"
GOOGLE_ANALYTICS = "UA-XXX"
GOOGLE_TAG_MANAGER = "GTM-XXX"

# CSS_FILE = 'main.css'
# Blogroll
# LINKS = (
#     ('Previous Blog', 'https://filipgorczynski.wordpress.com/'),
# )
# LINKS = ()
SOCIAL = (
    ("rss", "/blog/feeds/all.atom.xml"),
    ("facebook", "https://www.facebook.com/filipgorczynski/"),
    ("twitter", "https://twitter.com/filipgorczynski"),
    ("github", "https://github.com/filipgorczynski"),
    ("linkedin", "https://www.linkedin.com/in/filip-g%C3%B3rczy%C5%84ski-52b08270/"),
)

MENUITEMS = (
    ("Tech", "/tech.html"),
    ("Life", "/life.html"),
    ("Notes", "/notes.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://www.seyiobaweya.tech/articles/2020-01-20/personal-website-setup/
STATIC_PATHS = [
    'img', 'images', 'static',
]

PLUGIN_PATHS = ['/home/filip/src/Vendors/pelican-plugins']
PLUGINS = [
    'pelican_gist',
    'pelican-cover-image',
    'metadataparsing',
    'pelican_htmlmin',
    'related_posts',
    'post_stats',
    'i18n_subsites',
]

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# https://github.com/getpelican/pelican-plugins/tree/master/post_stats

# https://github.com/getpelican/pelican-plugins/tree/master/related_posts
RELATED_POSTS_MAX = 10

OG_LOCALE = "en_EN"
LOCALE = "en_EN"

# Default theme language.
I18N_TEMPLATES_LANG = "en"
# DATE_FORMATS = {
#     "en": "%B %d, %Y",
#     "pl": "%Y-%M-%d, %Y",
# }
EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}

# THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
# THEME_COLOR_ENABLE_USER_OVERRIDE = True

# USE_LESS = True