# фраирует endpoints url-адресов для приложений

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.conf.urls import include, url

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^api/', include('api.urls'))
]