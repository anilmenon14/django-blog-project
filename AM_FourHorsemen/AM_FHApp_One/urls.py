from django.conf.urls import url
from AM_FHApp_One import views

# Template tagging. This defines the app name passed in the template tag
app_name = 'AM_FHApp_One'

urlpatterns = [
    url(r'^relative/$' ,views.relative,name='relativeballs'),
    url(r'^other/$',views.other,name='other')
]
