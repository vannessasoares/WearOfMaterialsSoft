from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from bancadaweb.views import *


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^graph/', Graph.as_view(), name='graph'),
    url(r'^admin/', admin.site.urls),

    # Views de Analise de Desgaste
    url(r'^new/$'               , AnaliseDesgasteCreate.as_view(), name='new_analise'),
    url(r'^list/'               , AnaliseDesgasteList.as_view()  , name='list_analise'),
    url(r'^analise/detail/(?P<pk>\d+)/$', AnaliseDesgasteDetail.as_view(), name='detail_analise'),
    url(r'^analise/update/(?P<pk>\d+)/$', AnaliseDesgasteUpdate.as_view(), name='update_analise'),
    url(r'^analise/delete/(?P<pk>\d+)/$', AnaliseDesgasteDelete.as_view(), name='delete_analise'),


    #Login e Logout
    url(r'^$' , auth_views.login, name='login'),
    url(r'^$', auth_views.logout, {'next_page': '/'}, name='logout'),

]
