# -*- coding: utf-8 -*-
#
# Django settings for project '{{ cookiecutter.project_name }}'

from os import listdir
from os.path import abspath, dirname, isfile, join

gettext = lambda s: s

# Root of buildout project
BASE_DIR = dirname(dirname(abspath(__file__)))

# Django project
PROJECT_PATH = join(BASE_DIR, 'project')
VAR_PATH = join(BASE_DIR, 'var')

DEBUG = True

# To control whether or not to display marketing tags stuff
# At least used in 'skeleton.html'. This settings is exposed in every context
# template since its related context processor is enabled.
MARKETINGTAGS_ENABLED = DEBUG

# Https is never enabled on default and development environment, only for
# integration and production.
HTTPS_ENABLED = False

ADMINS = (
    #('Emencia', 'PUT_ADMIN_EMAIL_HERE'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Database name. Or path to database file if using sqlite3.
        'NAME': join(BASE_DIR, 'database.sqlite3'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',               # Empty for localhost through domain sockets
                                  # or '127.0.0.1' for localhost through TCP.
        'PORT': '',               # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*'] # FIXME Put here the domain names

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

LANGUAGES = (
    #("en-au", gettext(u"Australia")),
    #("de", gettext(u"Deutschland")),
    #("es", gettext(u"España")),
    ("fr", gettext(u"France")),
    #("zh-hk", gettext(u"Hong Kong")),
    #("it", gettext(u"Italia")),
    #("nl", gettext(u"Nederland")),
    #("pl", gettext(u"Polska")),
    #("ru", gettext(u"Россия")),
    #("en-gb", gettext(u"United Kingdom")),
    #("en", gettext(u"USA")),
    #("ja", gettext(u"日本")),
    #('zh-cn', gettext(u'中国')),
    #("ko-kr", gettext(u"한국")),
)
## More knowed country locales
#EXTRA_COUNTRY_LOCALES = LANGUAGES + (
    #("pt-br", gettext(u"Brasil")),
    #("es-cl", gettext(u"Chile")),
    #("es-co", gettext(u"Colombia")),
    #("cs", gettext(u"Czech Republic")),
    #("ar-ma", gettext(u"Morocco")),
    #("en-nz", gettext(u"New Zealand")),
    #("hu-si", gettext(u"Slovenia")),
    #("tr", gettext(u"Turkey")),
    #("ss-za", gettext(u"South Africa")),
#)

# A tuple of directories where Django looks for translation files
LOCALE_PATHS = (
    join(PROJECT_PATH, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ cookiecutter.secret_key }}'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            join(PROJECT_PATH, "templates"),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
            )
        }
    },
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIGRATION_MODULES = {}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'file_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': join(VAR_PATH, 'log', 'error.log')
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file_handler', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Otherwise uploaded files larger than FILE_UPLOAD_MAX_MEMORY_SIZE will be
# written with 0600 permissions, and so Nginx won't be able to serve them.
# This issue has been found with django-filebrowser-no-grappelli
FILE_UPLOAD_PERMISSIONS = 0644


#
# Mods system
#
def add_to_tuple(var, *args, **kw):
    """
    This utility method should be used to modify INSTALLED_APPS and the like.

    It features:

    * Avoid duplicates by checking whether the items are already there;
    * Add many items at once;
    * Allow to add the items before some other item, when order is important
      (by default it appends). If the before item does not exist, just insert
      the value at the end;

    Example:

        INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'foo', 'bar')

    Or:

        INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'fifi', 'loulou', before='riri')
    """
    before = kw.get('before')

    var = list(var)
    for arg in args:
        if arg not in var:
            if before and before in var:
                var.insert(var.index(before), arg)
            else:
                var.append(arg)

    return tuple(var)

# Shadow import using execfile for enabled mods
# With execfile, the python script will be executed in the current context and so
# can directly access to it (like using/modifying its variables)
mods = join(PROJECT_PATH, 'mods_enabled')
mods = [join(mods, x) for x in listdir(mods)]
mods.sort()
for MOD_FILE in mods:
    mod = join(MOD_FILE, 'settings.py')
    if isfile(mod):
        execfile(mod)
