from django.conf.urls import url,include
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    url(r'^post',csrf_exempt(views.post),name="post"),
    url(r'^(?P<username>[a-z,0-9,A-Z]+)$',views.userimages),
    url(r'^(?P<username>[a-z,0-9,A-Z]+)/(?P<imgname>[a-z,0-9,A-Z,\-,\.]+)$',views.serveimage),
    url(r'^$',views.index,name="form")
]
