from django.urls import path
from . import views
urlpatterns = [
   path('demo/', views.demo , name='demo'),
   path('country/', views.country , name='country'),
   path('province/', views.province, name='province'),
   path('trial/', views.trial, name='trial'),
   path('add_country/', views.add_country, name='add.country'),
   path('add_province/', views.add_province, name='add.province')
]