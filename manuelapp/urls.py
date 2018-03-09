from django.conf.urls import url
from manuelapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]