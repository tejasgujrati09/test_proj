
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$',views.home, name = 'home'),
    url(r'^data/$',views.save_data, name = 'sensor_data'),
    url(r'^about/$',views.about, name = 'about'),
]
