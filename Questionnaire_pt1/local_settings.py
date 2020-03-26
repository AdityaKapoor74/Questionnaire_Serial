SECRET_KEY = 'cs6k9*0r6biitovqfjc+88e3oxr=0vd(#l(siu=w_f79mr#bb%hello'

ALLOWED_HOSTS = ['174.138.37.34']

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'onebyone',
        'USER': 'aditya',
        'PASSWORD': 'Warmachine@42',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = False
