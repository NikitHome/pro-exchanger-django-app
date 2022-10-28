from unicodedata import name
from django.urls import path
from . import views

app_name = 'exchanger'
urlpatterns = [
    path('', views.index, name='index'),
    path('cooperation/', views.cooperation, name='cooperation'),
    path('contacts/', views.contacts, name='contacts'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('partners/', views.partners, name='partners'),
    path('rules/', views.rules, name='rules'),
    path('abot_us/', views.about_us, name='about_us'),
    path('exchange_rules/', views.exchange_rules, name='exchange_rules')
]