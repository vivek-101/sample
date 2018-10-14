from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^refrence/',views.refrence,name='refrence'),
    url(r'^home/',views.home,name='home'),
]
