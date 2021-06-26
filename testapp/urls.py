from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile),
    path('otherprofile', views.other),
    path('summary', views.summary),
    path('history', views.history),
    path('pool', views.pool),
    path('login', views.login),
    path('dashboard', views.dashboard),
] 