from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='MusicIndex'),
    path('albums/', views.albums, name='Albums'),
]
