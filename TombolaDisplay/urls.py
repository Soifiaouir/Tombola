from django.urls import path
from . import views

urlpatterns = [

    path('', views.user, name='Users'),
    path('Tombola/', views.index, name='index'),
    path('participant/<int:participant_id>/tombola', views.tombola_create, name='tombola'),
    path('participant/<int:participant_id>/tombola/<int:tombola_id>/get_ticket', views.get_ticket, name='get_ticket'),
]