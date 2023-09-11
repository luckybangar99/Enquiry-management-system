from django.urls import path
from  app import views


urlpatterns=[
    path('',views.home,name='home'),
    path('uregis/',views.uregis,name='uregis'),
    path('userdata/',views.users,name='userdata'),
    path('ulogin/',views.Login,name='ulogin'),
    path('udash/',views.userdata,name='udash'),
    path('aregis/',views.aregis,name='aregis'),
    path('admindata/',views.adminn,name='admindata'),
    path('alogin/',views.aLogin,name='alogin'),
    path('alogin/',views.adash,name='alogin'),
    path('adash/',views.Querydatadisplay,name='query'),
    path('udisp/',views.Userdatadisplay,name='udisp'),
    path('adisp/',views.Admindatadisplay,name='adisp'),
    
]