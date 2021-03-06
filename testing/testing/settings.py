# Copyright (c) 2010-2013 by Yaco Sistemas <goinnn@gmail.com> or <pmartin@yaco.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.


# Django settings for testing project.
import os
from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

BASEDIR = path.dirname(path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': path.join(BASEDIR, 'testing.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                       # Not used with sqlite3.
        'PASSWORD': '',                   # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
      ('es', 'Spanish'),
      ('en', 'English'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = path.join(BASEDIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/my_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '98qi@6+%3nt__m_o6@o(n8%+!)yjxrl*fcs%l@2g=e-*4fu4h%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

ALLOWED_HOSTS = [
    'localhost',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'testing.urls'

TEMPLATE_DIRS = (
    path.join(BASEDIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'inplaceeditform',
    'django.contrib.admin',
    'testing.multimediaresources',
    'testing.unusual_fields',
    'testing.unit_tests',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

# django-inplaceedit customization

#INPLACEEDIT_EDIT_EMPTY_VALUE = 'Double click to edit...'
#INPLACEEDIT_AUTO_SAVE = True
#INPLACEEDIT_EVENT = "click"
#INPLACEEDIT_DISABLE_CLICK = False
#INPLACEEDIT_EDIT_MESSAGE_TRANSLATION = 'Write a translation...'
#INPLACEEDIT_SUCCESS_TEXT = 'Successfully saved...'
#INPLACEEDIT_UNSAVED_TEXT = 'You have unsaved changes!!!!'
#INPLACE_ENABLE_CLASS = 'enable'
#DEFAULT_INPLACE_EDIT_OPTIONS = {}
#DEFAULT_INPLACE_EDIT_OPTIONS_ONE_BY_ONE = False
#ADAPTOR_INPLACEEDIT_EDIT = 'inplaceeditform.perms.AdminDjangoPermEditInline'
#ADAPTOR_INPLACEEDIT = {}
#INPLACE_GET_FIELD_URL = None
#INPLACE_SAVE_URL = None
#INPLACE_FIELD_TYPES = 'input, select, textarea'
#INPLACE_FOCUS_WHEN_EDITING = True


# If transmeta is installed
from django.conf import ENVIRONMENT_VARIABLE
# I check it if transmeta is installed of this way because if I execute
# python manage.py runserver --settings=settings_no_debug
# I get an error
if os.environ[ENVIRONMENT_VARIABLE] == 'testing.settings':
    try:
        import transmeta
        TRANSMETA_DEFAULT_LANGUAGE = 'en'
        INSTALLED_APPS += ('transmeta',
                           'testing.inplace_transmeta')
        MIDDLEWARE_CLASSES += (
            'django.middleware.locale.LocaleMiddleware',
            'testing.inplace_transmeta.middleware.LocaleMiddleware')
    except ImportError:
        pass

# If inplaceeditform_extra_fields is installed

try:
    import inplaceeditform_extra_fields
    INSTALLED_APPS += ('inplaceeditform_extra_fields',
                       'testing.example_extra_fields')
    ADAPTOR_INPLACEEDIT = {'auto_fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
                           'auto_m2m': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField',
                           'image_thumb': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
                           'tiny': 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField',
                           'tiny_simple': 'inplaceeditform_extra_fields.fields.AdaptorSimpleTinyMCEField',
                           }
    try:
        import ajax_select
        INSTALLED_APPS += ('ajax_select',)
        AJAX_LOOKUP_CHANNELS = {
            'typeresource': {'model': 'multimediaresources.typeresource',
                             'search_field': 'name'},
            'user': {'model': 'auth.user',
                     'search_field': 'username'},
        }
    except ImportError:
        pass
    try:
        import sorl
        INSTALLED_APPS += ('sorl.thumbnail',)
        THUMBNAIL_DEBUG = DEBUG
    except ImportError:
        pass
except ImportError:
    pass


# Custom settings to the different django versions

import django

if django.VERSION[0] >= 1 and django.VERSION[1] >= 4:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.tz',)

if django.VERSION[0] >= 1 and django.VERSION[1] >= 3:
    INSTALLED_APPS += ('django.contrib.staticfiles',)
    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = path.join(BASEDIR, 'static')

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = '/static/admin/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.static',)

if django.VERSION[0] >= 1 and django.VERSION[1] >= 2:
    INSTALLED_APPS += ('django.contrib.messages',)
    MIDDLEWARE_CLASSES += ('django.middleware.csrf.CsrfViewMiddleware',
                           'django.contrib.messages.middleware.MessageMiddleware')
    TEMPLATE_CONTEXT_PROCESSORS += ('django.contrib.messages.context_processors.messages',)
