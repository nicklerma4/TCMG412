#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ayo Okunnu, Alec Azar, Ebenezer Zabayor, Nicholas Lerma'
SITENAME = 'TCMG412 Project 1'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'pelican-themes/blueidea'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']
STATIC_PATHS = ['images']
SUMMARY_MAX_LENGTH = 60
DEFAULT_PAGINATION = 10
GITHUB_URL = 'https://github.com/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('VoxPol', 'https://www.voxpol.eu/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
