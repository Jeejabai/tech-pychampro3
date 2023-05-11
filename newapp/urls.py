from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reg', views.reg, name='reg'),
    path('reg1', views.reg1, name='reg1'),
    path('log', views.log, name='log'),
    path('valid', views.valid, name='valid'),
    path('about', views.about, name='about'),
    path('home1', views.home1, name='home1'),
    path('serform', views.serform, name='serform'),
    path('service', views.service, name='service'),
    path('proform', views.proform, name='proform'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    path('service1', views.service1, name='service1'),
    path('supdate/<int:id>/', views.supdate, name='supdate'),
    path('sde/<int:id>/', views.sde, name='sde'),
    path('project1', views.project1, name='project1'),
    path('pupdate/<int:id>/', views.pupdate, name='pupdate'),
    path('prd/<int:id>/', views.prd, name='prd'),
    path('newabt', views.newabt, name='newabt'),

]
