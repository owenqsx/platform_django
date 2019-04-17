from django_base.base_settings import *

# Application definition

INSTALLED_APPS += [
    'django_base.base_config',
    'django_base.base_geo',
    'django_base.base_mark',
    'django_base.base_media',
    'django_base.base_member',
    'django_base.base_meta',
    # 'apps.goods',
    # 'apps.institution',
    # 'apps.member',
    # 'apps.order',
    # 'apps.posts',
    # 'apps.pricing',
    # 'apps.core',
    # 'apps.inventory',
    # 'apps.finance',
    # 'apps.erp_bridge',
    # 'apps.tests',
    # 'apps.share',
    # 'apps.report',
    # 'apps.order_aggregation',
    # 'apps.order_customization',
    # 'apps.industrial_customer',
    # 'apps.coupon',
    # 'dbdoc',
]

MIDDLEWARE += [
]

MIDDLEWARE.remove('django.middleware.csrf.CsrfViewMiddleware')
#
# CSRF_COOKIE_SECURE = False
# print(MIDDLEWARE)

WSGI_APPLICATION = 'platform_py.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]

# ============== URLS ================

# ROOT_URLCONF = 'apps.core.urls'
ROOT_URLCONF = 'platform_py.urls'
ENABLE_ADMIN_SITE = True
ENABLE_APP_FRONT_API = True
ENABLE_PC_FRONT_API = True

# ============== REST FRAMEWORK ================

# REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'apps.core.exceptions.exception_handler'

# =========== CRON =======================

# CRON_CLASSES = [
#     'apps.core.cron.SyncErpCronJob'
# ]

# =============== SMS Config ===================

SMS_ACCESS_KEY_ID = 'LTAIlVWi3nF31eOx'
SMS_ACCESS_KEY_SECRET = 'zInMLFpWjQgiFWDdzBwTQS7fWxAa5Y'

# SMS_APPKEY = '23405490'
# SMS_SECRET = 'fc4dde7fe3659364293bd830d334e3a4'
# SMS_TEMPLATE_CODE = {'validate': 'SMS_12225993'}
SMS_SEND_INTERVAL = 60  # 短信发送时间间隔限制
SMS_EXPIRE_INTERVAL = 1800
SMS_SIGN_NAME = '悍高云商'
SMS_TEMPLATES = dict(
    # AUTH='SMS_142655056',
    # LOGIN_CONFIRM='SMS_142655055',
    # LOGIN_EXCEPTION='SMS_142655054',
    # USER_REGISTER='SMS_142655053',
    # CHANGE_PASSWORD='SMS_142655052',
    # UPDATE_INFO='SMS_142655051',
    SIGN_IN='SMS_142655055',
    CHANGE_PASSWORD='SMS_142655052',
    CHANGE_MOBILE_VERIFY='SMS_142655051',
    CHANGE_MOBILE_UPDATE='SMS_142655056',
)
SMS_DEBUG = True  # 不真正发送短信，将验证码直接返回

# =============== WeChat API Root =================

WECHAT_API_ROOT = 'http://wx.easecloud.cn'

# =============== K/3 ERP Database Connection ================

# ERP_API_ROOT = 'http://61.145.96.204:8088/'
# ERP_API_APPID = '10000'

# =============== DB DOC ================

# import apps.erp_bridge.models
# import apps.finance.models
# import apps.goods.models
# import apps.institution.models
# import apps.inventory.models
# import apps.member.models
# import apps.order.models
# import apps.posts.models
# import apps.pricing.models
# import apps.share.models

# DBDOC_MODELS = [
#     'apps.goods.models',
#     'apps.institution.models',
#     'apps.member.models',
#     'apps.order.models',
#     'apps.posts.models',
#     'apps.pricing.models',
#     'apps.core.models',
#     'apps.inventory.models',
#     'apps.finance.models',
#     'apps.erp_bridge.models',
#     'apps.tests.models',
#     'apps.share.models',
#     'apps.report.models',
#     'apps.order_aggregation.models',
#     'apps.order_customization.models',
#     'apps.industrial_customer.models',
# ]
