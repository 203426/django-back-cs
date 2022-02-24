from django.urls import path, re_path
from django.conf.urls import include


# Importacion de la vista
from register.views import RegistroView

urlpatterns = [
    re_path(r'^registro_nuevo/$', RegistroView.as_view())
]