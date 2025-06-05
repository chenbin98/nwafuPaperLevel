# goodjournal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_journal, name='search'),
    path('update/', views.update_journal, name='update'),
]