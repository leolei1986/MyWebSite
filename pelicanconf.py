#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '雷舰'
SITENAME = '我的站点'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'#'zh'
THEME = "../pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "flatly"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']
#I18N_TEMPLATES_LANG = 'en'
LOAD_CONTENT_CACHE = False
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#DELETE_OUTPUT_DIRECTORY = True
#DELETE_RETENTION = [".git"]
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com'),
         ('Python.org', 'http://python.org'),
         ('Bootswatch', 'https://bootswatch.com'),
         ('Jinja2', 'http://jinja.pocoo.org'),
         )

# Social widget
SOCIAL = (('My Github', 'https://github.com/leolei1986'),
        ('My CSDN blog', 'https://blog.csdn.net/cherishlei'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#static paths will be copied without parsing their contents
#STATIC_EXCLUDE_SOURCES = False
STATIC_PATHS = [
        'search.html',
        ]
