AUTHOR = 'Jeffrey McAteer'
SITENAME = 'Playground'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Source Code", "https://github.com/Jeffrey-P-McAteer/pelican-playground"),
)

# Social widget
#SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
#)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME_TEMPLATES_OVERRIDES = [ 'theme-overrides' ]

STATIC_PATHS = [
    'images',
    'static'
]

STORK_OUTPUT_OPTIONS = {
    'debug': True,
}
