from django.conf.urls import url
from manuelapp import views


urlpatterns = [
    url(r'^$', views.index_models, name='index_models'),
]