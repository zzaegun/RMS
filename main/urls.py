from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^login/$', views.login, name='login'),
    url(r'^cReq/$', views.cReq, name='cReq'),
    url(r'^cList/$', views.cList, name='cList'),
    url(r'^cModify/$', views.cModify, name='cModify'),
    url(r'^aPur/$', views.aPur, name='aPur'),
    url(r'^aPurMan1/$', views.aPurMan1, name='aPurMan1'),
    url(r'^aPurMan2/$', views.aPurMan2, name='aPurMan2'),
    url(r'^aPurMan3/$', views.aPurMan3, name='aPurMan3'),
    url(r'^admin1/$', views.admin1, name='admin1'),
    url(r'^admin2/$', views.admin2, name='admin2'),
    url(r'^notwk/$', views.notwk, name='notwk'),   
    
    url(r'^cReq_newRequest/$', views.cReq_newRequest, name='cReq_newRequest'),
    #url('/', include())
]