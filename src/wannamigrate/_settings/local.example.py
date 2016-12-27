"""
Local Settings file ignored by GIT so that we do not expose sensitive information

Remember to remove the ".example" from the file name
"""

#########################################
# DJANGO ENVIRONMENT CONFIGURATION
#########################################

# DJANGO SECURITY KEY (This need to be unique for the project)
SECRET_KEY = ''

# Debug
IS_PROD = False
DEBUG = True
SQL_DEBUG = False


#########################################
# DATABASE AUTH
#########################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'thewinegallery',
        'USER': 'thewinegallery',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


#########################################
# SOMMELIER AUTH
#########################################
if IS_PROD:
    SOMMELIER_URL = 'http://sommelier.thewinegallery.com.au/'
    SOMMELIER_SECRET_KEY = ''
else:
    SOMMELIER_URL = 'http://sommelier.thewinegallery.com.au/'
    SOMMELIER_SECRET_KEY = ''


#########################################
# PAYMENT AUTH
#########################################
STRIPE_URL = 'https://api.stripe.com'
if IS_PROD:
    STRIPE_SECRET_KEY = ''
    STRIPE_PUBLISHABLE_KEY = ''
else:
    STRIPE_SECRET_KEY = ''  # TEST KEY
    STRIPE_PUBLISHABLE_KEY = ''  # TEST KEY


#########################################
# SHIPPING AUTH
#########################################
if IS_PROD:
    SHIPPIT_URL = 'https://shippit.com/api/3/'
    SHIPPIT_SECRET_KEY = ''
else:
    SHIPPIT_URL = 'https://staging.shippit.com/api/3/'  # TEST ENDPOINT
    SHIPPIT_SECRET_KEY = ''  # TEST KEY
