from django.conf.urls import url, include
from factory_ui import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate_yaml', views.generate_yaml),
    url(r'^build_api_from_yaml', views.build_api_from_yaml)



]
