from django.urls import path
from . import views
urlpatterns = [
    path('',views.header,name='inicio'),
    path('nosotros/', views.nosotros,name='nosotros'),
    path('cursos/',views.cursos,name='cursos'),
    path('publicaciones/',views.publicaciones,name='publicaciones')
]
