from pictures import views
from django.conf.urls import url

urlpatterns = [
    url(r'^show-ngo-child/$', views.ShowNGOChild.as_view()),
]