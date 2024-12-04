
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # page d'administration django
    path('', views.accueil, name='accueil'), # page d'accueil 
    path('connexion/', views.connexion, name="connexion"), # page de connexion
    path('Apropos/', views.Apropos, name="Apropos"), # page à propos
    path('reinit/', views.reinit, name="reinit"), # page de réinitialisation de mot de passe
    path('index/', views.index, name="index"), # tableau de bord administrateur 
    path('eleve/', views.eleve, name="eleve"), # tableau de bord eleves
    path('prof/', views.prof, name="prof"), # tableau de bord prof
    path('Liste_eleves/', views.Liste_eleves, name="Liste_eleves"), # liste des élèves
    path('Listes_eleves/', views.Listes_eleves, name="Listes_eleves"), # liste des élèves vue admin
    path('Liste_prof/', views.Liste_prof, name='Liste_prof'), # liste des profs
    path('prof_add/', views.prof_add, name='prof_add'), # page d'admission des profs 
    path('eleve_add/', views.eleve_add, name='eleve_add'), # page d'admission des élèves 
    path ('toute_classe', views.toute_classe, name='toute_classe'), # toutes les classes
    path('Liste_parent/', views.Liste_parent, name='Liste_parent' ), # liste des parents
    path('toutes_classes/', views.toutes_classes, name='toutes_classes'), # liste des classes vue de profs
    path('liste_classes_eleves/<int:classe_id>/', views.liste_classe_eleves, name='liste_classe_eleves'), 
    path('prof/<int:professeur_id>/', views.detail_prof, name='detail_prof'),
    path('prof_add/sites/teacher-details/<int:professeur_id>/', views.detail_prof, name='detail_prof'),
    path('eleve_add/sites/student-details/', views.eleve_detail, name='eleve_detail'),
    path('reçu/', views.reçu, name="reçu"),
    path('prof_add/sites/teacher-details.html/', views.detail_prof, name='detail_prof'),
    path('detail_prof/',views.detail_prof, name='detail_prof'), # détails des profs 
    path('inscription/', include('inscription.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])




    # path('eleve_add/sites/student-details.html/', views.reçu, name="reçu"),
    # path('eleve_add/sites/student-details.html/<int:pk>/',views.eleve_detail, name="eleve_detail"),
    # path('eleve_add/sites/student-details.html',views.eleve_detail, name="eleve_detail"),
    # path('eleve_add/<int:pk>/sites/student-details.html/', views.eleve_detail, name='eleve_detail'),
