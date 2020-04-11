DEBUG = False
ALLOWED_HOSTS = ['thegradientboost.com','www.thegradientboost.com','localhost','162.213.250.25']

#mssql database requirements for production use
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
 


# EMAIL_HOST = 'mail.privateemail.com'
# # 'mail.privateemail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = 'emmanuel@thegradientboost.com'
# EMAIL_HOST_PASSWORD = 'K@leidoscope69'


#update your data
#https://myaccount.google.com/u/0/lesssecureapps?pli=1&pageId=none

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "emmanuels@thegradientboost.com"
EMAIL_HOST_PASSWORD = "K@leidoscope69"


#for admin email
C_SITE_URL = 'thegradientboost.com'
