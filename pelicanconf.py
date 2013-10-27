#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcin Jabrzyk'
SITENAME = u'Marcin Jabrzyk'
SITEURL = 'http://localhost:8000'

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['interlinks', 
	   'sitemap', 
	   'summary',
	   'pelican_youtube',]
#better_figures_and_images


TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/bzyx'),
	  ('github', 'https://github.com/bzyx'),
          ('linkedin', 'https://www.linkedin.com/in/marcinjabrzyk'),   
          ('google-plus', 'https://plus.google.com/113868949402441845973/'),
          ('rss', 'http://feeds.feedburner.com/bzyx'),
          )

ABOUT = u"I'm developer of embedded systems, interested especially in embedded Linux. <br/> \
	  Skilled in Python, C, C++ and Qt framework. Mostly writting <abbr title='AVR, ARM'>embeeded</abbr> software and <abbr title='Linux, Windows'>desktop</abbr> apps, co-organizer of IT <abbr title='SmartDevCon, PyconPL'> conferences.</abbr> \
	  Master degree student at <abbr title='Silesian University of Technology'>SUT</abbr>."
	  

DEFAULT_PAGINATION = 6
TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

GITHUB_USER = 'bzyx'
#GITHUB_SHOW_USER_LINK = False
#GITHUB_REPO_COUNT = True
#GITHUB_SKIP_FORK = True

ADDTHIS_PROFILE = 'ra-525841e026fe56fc'

USE_OPEN_GRAPH = False
#OPEN_GRAPH_FB_APP_ID = '216827641826380'


ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'

DEFAULT_DATE_FORMAT = "%d/%m/%Y"

STATIC_PATHS = ['images', 'extras/CNAME']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = 'marcinjabrzyk'
