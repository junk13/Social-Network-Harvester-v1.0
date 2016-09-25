"""
Django settings for SocialNetworkHarvester_v1p0 project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import logging
from .logger import Logger
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print('BASE_DIR: '+BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# To generate a secure key, you can use a webservice such as http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/login_page'

FACEBOOK_APP_PARAMS = {
    'app_id':'',
    'version':'v',
    'secret_key':''}

YOUTUBE_VIDEOS_LOCATION = '' # Absolute path to folder

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SocialNetworkHarvester_v1p0',
    'AspiraUser',
    'Facebook',
    'Group',
    'tool',
    'Twitter',
    'Youtube',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SocialNetworkHarvester_v1p0.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/SocialNetworkHarvester_v1p0/templates/',
            BASE_DIR + '/AspiraUser/templates/',
            BASE_DIR + '/DailyMotion/templates/',
            BASE_DIR + '/Facebook/templates/',
            BASE_DIR + '/Group/templates/',
            BASE_DIR + '/tool/templates/',
            BASE_DIR + '/Twitter/templates/',
            BASE_DIR + '/Youtube/templates/',
        ],
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

WSGI_APPLICATION = 'SocialNetworkHarvester_v1p0.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'snh_2016_schema',                
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            'OPTIONS': {
                "init_command": "SET foreign_key_checks = 0;",
                "charset":"utf8mb4"
            }
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'staticfiles'),)

LOG_DIRECTORY = os.path.join(BASE_DIR,"log")

###### LOGERs ######
twitterLogger = Logger(loggerName='twitterLogger', filePath=os.path.join(LOG_DIRECTORY,"twitter.log"),
                    append=True, indentation=0, showThread=True)
facebookLogger = Logger(loggerName='facebookLogger', filePath=os.path.join(LOG_DIRECTORY, "facebook.log"),
                       append=True, indentation=0, showThread=False)
youtubeLogger = Logger(loggerName='youtubeLogger', filePath=os.path.join(LOG_DIRECTORY, "youtube.log"),
                       append=False, indentation=0, showThread=True)
viewsLogger = Logger(loggerName='viewsLogger', filePath=os.path.join(LOG_DIRECTORY,"views.log"),
                    append=True, indentation=2)

######### EMAIL SETTINGS #########

EMAIL_HOST = ""
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True
EMAIL_PORT = 465

