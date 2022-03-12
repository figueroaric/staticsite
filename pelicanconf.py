AUTHOR = 'Ricardo Figueroa'
SITENAME = 'Static Site Test'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

#pelicanconf.py

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup


PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

#PLUGIN_PATHS = ['/path/to/git/pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites', 'series','tag_cloud','liquid_tags.youtube','liquid_tags.notebook','liquid_tags.include_code','render_math','pelican-ipynb.markup',nb_markup]

I18N_TEMPLATES_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = True

IGNORE_FILES = [".ipynb_checkpoints"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True