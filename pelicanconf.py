#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import date


AUTHOR = 'Karo'
SITENAME = 'A blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'
LOCALE = 'en_US.utf8'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/'

# Theme customizations
MINIMALXY_FAVICON = './images/extra/favicon.ico'
MINIMALXY_START_YEAR = 2021
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Karo. PyLadies & Python. Languages. Moravia'
AUTHOR_DESCRIPTION = u'Hi there! I’m Karo. Whenever not computering, I read yet another book or hike through South Moravia.'
AUTHOR_AVATAR = './images/extra/karo.jpg'
AUTHOR_WEB = 'https://karolinasurma.eu'


# Social
SOCIAL = (
    ('github', 'https://github.com/befeleme'),
    ('linkedin', 'https://www.linkedin.com/in/karolina-surma-950452b7/'),
)

# Menu
CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_SAVE_AS = 'archives.html'
MENUITEMS = (
    ('Categories', '/' + CATEGORIES_SAVE_AS),
    ('Archive', '/' + ARCHIVES_SAVE_AS),
)