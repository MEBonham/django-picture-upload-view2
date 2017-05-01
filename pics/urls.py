from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^([0-9]+)/$', views.picture, name='picture'),
    url(r'upload', views.upload, name='upload'),
]