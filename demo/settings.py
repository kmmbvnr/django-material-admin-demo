import os
from oscar import get_core_apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lkmmbxp03s_1!l8@b@#!7#udm98+ca@#@s)rm5_zu(2u5(wc%d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'material',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # deps
    'mptt',
    'sekizai',
    'compressor',
    'django_extensions',
    'easy_thumbnails',
    'guardian',

    # TODO 'userena',
    # TODO 'zinnia',
    # TODO 'django_q''
    # TODO 'pushy'
    # TODO 'river'

    # admin demo
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'dbmail',
    'django_comments',
    'organizations',
    'registration',
    'social.apps.django_app.default',
    'watson',
    'report_builder',
    'timepiece',
    'push_notifications',
    'djstripe',
    'paypal.pro',
    'pinpayments',
    'axes',
    'robots',
    'djangoseo',
    'constance',
    'dynamic_preferences',
    'taggit',
    'djcelery',
    'wiki',
    'waliki',
    'viewflow',
    'actstream',
    'dynamic_scraper',
    'explorer',
    # 'cms',
    # 'mezzanine.accounts',
    # 'mezzanine.blog',
    # 'mezzanine.core',
    # 'mezzanine.forms',
    # 'mezzanine.galleries',
    # 'mezzanine.generic',
    # 'mezzanine.pages',
    # 'mezzanine.twitter',
    # 'wagtail.wagtailforms',
    # 'wagtail.wagtailredirects',
    # 'wagtail.wagtailembeds',
    # 'wagtail.wagtailsites',
    # 'wagtail.wagtailusers',
    # 'wagtail.wagtailsnippets',
    # 'wagtail.wagtaildocs',
    # 'wagtail.wagtailimages',
    # 'wagtail.wagtailsearch',
    # 'wagtail.wagtailadmin',
    # 'wagtail.wagtailcore',
    # ] + get_core_apps()
]

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# Various dumb settings
ANONYMOUS_USER_ID = -1
ACCOUNT_ACTIVATION_DAYS = 10
COMPRESS_ROOT = os.path.join(BASE_DIR, 'cache')
SENTRY_USE_BIG_INTS = False
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
    },
}
STRIPE_SECRET_KEY = 'XXXX-XXX-XXXX'
PIN_ENVIRONMENTS = {
    'test': {
        'key': 'pk_qokBvPpEHIVmNETSoSdDVYP',
        'secret': 'MBjZMurpDtjDANDNFQObZmBhMg',
        'host': 'test-api.pin.net.au',
    },
}
PACKAGE_NAME_FILEBROWSER = "filebrowser"
TESTING = False
OSCAR_REQUIRED_ADDRESS_FIELDS = ()
OSCAR_IMAGE_FOLDER = os.path.join(BASE_DIR, 'cache')
OSCAR_PROMOTION_FOLDER = os.path.join(BASE_DIR, 'cache')
OSCAR_MODERATE_REVIEWS = False
OSCAR_DELETE_IMAGE_FILES = False
OSCAR_EAGER_ALERTS = True
OSCAR_SLUG_MAP = {}
OSCAR_SLUG_BLACKLIST = []
