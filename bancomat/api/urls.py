# формирует url-адреса для api

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.conf.urls import url
from .views import Bancomat

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

banc = Bancomat()

urlpatterns = [
    url(r'^banc/set$', banc.set),
    url(r'^withdraw$', banc.get),
    url(r'^bank/status$', banc.status)
]