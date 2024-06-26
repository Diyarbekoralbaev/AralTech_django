from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e3dd6b4b3bd0a3965832bf3665a1481b06aeb0176f8c887a448ffe7cfed8f657'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://araltech.tech', 'https://www.araltech.tech']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'aral_app',

    # 'axes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'AralTech_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'AralTech_portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# AUTHENTICATION_BACKENDS = [
#     'axes.backends.AxesStandaloneBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title": "AralTech",
    "site_header": "AralTech",
    "site_logo": None,
    "login_logo": None,
    "welcome_sign": "Welcome to Aral Sea website admin panel",
    "copyright": "AralTech Ltd",
        "usermenu_links": [
        {"name": "Contact to developer", "url": "https://t.me/AralTech_Dev", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_title": True,
    "show_sidebar": True,
    "navigation_expanded": False,
    "search_bar": True,
    "show_ui_builder": True,
}

AXES_FAILURE_LIMIT = 3  # Number of login attempts allowed before lockout
AXES_LOCK_OUT_AT_FAILURE = True  # Whether to lock out after too many login attempts
AXES_COOLOFF_TIME = 10  # Number of minutes to lock out the user
# AXES_ENABLE_ADMIN = True  # Whether to display the admin site
# AXES_LOCKOUT_URL = ' lockout
# AXES_RESET_ON_SUCCESS = True  # Attempt to automatically unlock the user based on configuration

