# формирует url-адреса для api

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.conf.urls import url
from .views import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^banc/set$', add_cash),
    url(r'^banc/withdraw$', withdraw_cash),
    url(r'^banc/status$', banc_status)
]