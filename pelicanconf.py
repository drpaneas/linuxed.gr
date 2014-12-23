#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import platform

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

########################### General Settings ###################################

AUTHOR = u'Panos Georgiadis'
SITENAME = u'L I N U X E D'
SITESUBTITLE = u"Ένα blog αφιερωμένο στο Linux και το Open Source."
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = u'el'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing 
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
	 ('unix stack exchange', 'http://unix.stackexchange.com/'),
	 ('nixCraft Tutorials', 'http://www.cyberciti.biz/faq/'),
	 ('nixsrv', 'https://nixsrv.com/llthw'),
	 ('sysadmin casts', 'https://sysadmincasts.com/'),
	 ('doctor android', 'http://doctorandroid.gr/'),
	 ('deltahacker', 'http://deltahacker.gr/'),
        )

# Social widget
SOCIAL = (
	  ('github', 'https://github.com/drpaneas/linuxed.gr'),
          ('twitter', 'https://twitter.com/PanosGeorgiadis/'),
          ('linkedin', 'https://gr.linkedin.com/in/panosgeorgiadis/'),
          ('google+', 'https://plus.google.com/+PanosGeorgiadis/posts'),    
          ('professional site', 'http://panosgeorgiadis.com/cv-resume-about'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css', 'extra/href_scroll.js', 'extra/jquery.zoom.js']
EXTRA_PATH_METADATA = {'extra/custom.css':{'path':'static/custom.css'},
                    'extra/href_scroll.js':{'path':'theme/js/href_scroll.js'},
                    'extra/jquery.zoom.js':{'path':'theme/js/jquery.zoom.js'},
                       }
for k in EXTRA_PATH_METADATA.keys(): # Fix backslash paths to resources if on Windows
    EXTRA_PATH_METADATA[system_path(k)] = EXTRA_PATH_METADATA.pop(k)


##################### Exterior Services ############################
DISQUS_SITENAME = 'linuxedgr'
DISQUS_SHORTNAME = 'linuxedgr'
DISQUS_DISPLAY_COUNTS = True

#GOOGLE_ANALYTICS = "UA-57661864-1"

ADDTHIS_PROFILE = 'ra-548e3c553a19ddf3'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False


####################### Theme-Specific Settings #########################
THEME = 'pelican-bootstrap3'#'html5-dopetrope'

# Pelican Theme-Specific Variables  
BOOTSTRAP_THEME = 'cosmo'#'sandstone'#'lumen'
SHOW_ARTICLE_CATEGORY = True

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'

ABOUT_ME = "Είμαι μηχανικός αυτοματισμού, δικτύων και προγραμματιστής. Ζω στην Νυρεμβέργη, και εργάζομαι στην <a href=\"https://www.suse.com\">SUSE Linux</a> \
<p>Περισσότερα για μένα <strong><a href=\"http://panosgeorgiadis.com\" title=\"προσωπικό website\">panosgeorgiadis.com</a></strong></p>\
<p>Στείλε μου " + """<a href="http://www.google.com/recaptcha/mailhide/d?k=01LH1gOAhxE28Ox7OsdvErgw==&amp;c=BSpEioonKQfn4LENsgaUuuynPzcSun1HlW9Pc0_-B3c=" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k\07501LH1gOAhxE28Ox7OsdvErgw\75\75\46c\75BSpEioonKQfn4LENsgaUuuynPzcSun1HlW9Pc0_-B3c\075', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Εμφάνισε την δίευθυνση e-mail"><strong>mail</strong></a></p>"""
AVATAR = "/images/headshot.png"

BANNER = "/images/banner.jpg"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
TAG_CLOUD_MAX_ITEMS = 8

PYGMENTS_STYLE = 'monokai'

############################ Plugins ######################################
PLUGIN_PATHS = ['plugins']
PLUGINS = ['simple_footnotes', 'extract_toc', 'feed_summary']
#PLUGINS = ['feed_summary']
FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100

MD_EXTENSIONS = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']
