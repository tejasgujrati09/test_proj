
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^data/$',views.home, name = 'home'),
]
