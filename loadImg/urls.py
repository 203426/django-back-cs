from django.urls import path, re_path
from django.conf.urls import include

# View
from loadImg.views import LoadImgTable,LoadImgTableDetail

urlpatterns = [
    re_path(r'^img/$', LoadImgTable.as_view()),
    re_path(r'^img/(?P<pk>\d+)$', LoadImgTableDetail.as_view()),    
]