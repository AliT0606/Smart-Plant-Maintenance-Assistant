from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('giris/', views.giris, name='giris'),
    path('kayit/', views.kayit, name='kayit'),
    path('cikis/', views.cikis, name='cikis'),

    path('panel/', views.panel, name='panel'),
    path('profil/', views.profil, name='profil'),
    path('kutuphane/', views.kutuphane, name='kutuphane'),
    path('takvim/', views.takvim, name='takvim'),
    path('istatistik/', views.istatistik, name='istatistik'),
    path('ai-teshis/', views.ai_teshis, name='ai_teshis'),
    path('yardim/', views.yardim, name='yardim'),
    path('gizlilik/', views.gizlilik, name='gizlilik'),

    # AJAX endpoints
    path('bitki/<int:plant_id>/sula/', views.sula, name='sula'),
    path('bitki/<int:plant_id>/not/', views.not_guncelle, name='not_guncelle'),
]
