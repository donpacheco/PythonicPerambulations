#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Jake Vanderplas'
SITENAME = u'Pythonic Perambulations'
SITESUBTITLE = u'Musings and ramblings through the world of Python'
SITEURL = ''#http://jakevdp.github.io'

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archive', 'archives.html')]
NEWEST_FIRST_ARCHIVES = True

#Github include settings
GITHUB_USER = 'jakevdp'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# STATIC_OUT_DIR requires pelican 3.3
STATIC_OUT_DIR = 'downloads'
STATIC_PATHS = ['images', 'figures', 'videos', 'code', 'notebooks']


# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = '/home/vanderplas/Opensource/pelican-octopress-theme/'
PLUGIN_PATH = '/home/vanderplas/Opensource/pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook']


# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
EXTRA_HEADER = open('_nb_header_mod.html').read().decode('utf-8')