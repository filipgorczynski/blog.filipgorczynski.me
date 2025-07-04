#!/usr/bin/env python
# https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example

AUTHOR = 'Filip Górczyński'
SITENAME = 'Filip Górczyński Blog'
SITEURL = 'https://blog.filipgorczynski.me'
SITETITLE = "Filip Górczyński"
SITESUBTITLE = "Jack of all trades; Master of none."
SITEDESCRIPTION = "Jack of all trades; Master of none."
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = "favicon.png"
BROWSER_COLOR = "#efefef"
ROBOTS = "index, follow"
# PATH = 'content'
TIMEZONE = 'UTC'
# DEFAULT_LANG = 'en'
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}
CUSTOM_CSS = "static/custom.css"
THEME='theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
COPYRIGHT_YEAR = 2025
COPYRIGHT_PERSONAL_NAME = "Filip Górczyński"
# PAGE_URL = '/pages/{slug}.html'
PAGE_URL = '/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'
# PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '/category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = '/tag/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = '/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
HOME_HIDE_TAGS = True
MAIN_MENU = True

GOOGLE_ANALYTICS = "UA-XXX"
GOOGLE_TAG_MANAGER = "G-6CT399TS6J"

# CSS_FILE = 'main.css'
# Blogroll
LINKS = (
    ('Previous Blog', 'https://filipgorczynski.wordpress.com/'),
    ('SynApps Software', 'https://synapps.software/'),
)
# LINKS = ()
SOCIAL = (
    ("github", "https://github.com/filipgorczynski"),
    ("rss", "/blog/feeds/all.atom.xml"),
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
# STATIC_PATHS = [
#     'images',  'featured', 'logos', # 'content', 'featured', 'logos' 'pdfs', 'static', 'zipfiles'
# ]

PLUGIN_PATHS = ['/home/filip/src/Vendors/pelican-plugins']
PLUGINS = [
    'pelican_gist',
    'metadataparsing',
    # 'extended_meta',
    # 'pelican_htmlmin',
    # 'related_posts',
    # 'post_stats',
    # 'i18n_subsites',
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

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
