
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name="connexion"),
    path('Apropos/', views.Apropos, name="Apropos"),
    path('reinit/', views.reinit, name="reinit"),
    path('index/', views.index, name="index"),
    path('eleve/', views.eleve, name="eleve"),
    path('prof/', views.prof, name="prof"),
    path('Liste_eleves/', views.Liste_eleves, name="Liste_eleves"),
    path('Liste_prof/', views.Liste_prof, name='Liste_prof'),
    path('prof_add/', views.prof_add, name='prof_add'),
    path('eleve_add/', views.eleve_add, name='eleve_add'),
    path ('Liste_prof/', views.Liste_prof, name='Liste_prof'),
    path ('toute_classe', views.toute_classe, name='toute_classe'),
    path('Liste_parent/', views.Liste_parent, name='Liste_parent' ),
    path('toutes_classes/', views.toutes_classes, name='toutes_classes'),
    path('liste_classes_eleves/<int:classe_id>/', views.liste_classe_eleves, name='liste_classe_eleves'), ######










    path('reçu/', views.reçu, name="reçu"),
    path('eleve_add/sites/student-details.html/', views.reçu, name="reçu"),
    path('eleve_add/sites/student-details.html/<int:pk>/',views.eleve_detail, name="eleve_detail"),
    path('eleve_add/sites/student-details.html',views.eleve_detail, name="eleve_detail"),
    path('prof_add/sites/teacher-details.html/', views.detail_prof, name='detail_prof'),
    path('detail_prof/',views.detail_prof, name='detail_prof'),
    
    path('eleve_add/<int:pk>/sites/student-details.html/', views.eleve_detail, name='eleve_detail'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
