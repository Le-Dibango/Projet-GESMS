
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('liste_appel/', views.liste_appel, name='Liste_appel'),
    path('confirmation_appel/', views.confirmation_appel, name='confirmation_appel'),
    # path('liste_appel/<int:id>/', views.liste_appel, name='liste_appel'),
]

