# формирует url-адреса для api

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.conf.urls import url
from .views import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^set$', add_cash),
    url(r'^withdraw$', withdraw_cash),
    url(r'^status$', banc_status)
]