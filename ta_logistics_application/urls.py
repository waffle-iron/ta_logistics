from django.conf.urls import url
from . import views
import oauth2client.contrib.django_util.site as django_util_site
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='application'),
    #url(r'^oauth2/', url(django_util_site.url))
]