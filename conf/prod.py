from conf.default import *


import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

MAILCHIMP_MAIN_LIST_ID = '76e29973e0'
