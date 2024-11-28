from django.urls import path
from app import views

#Rotas utilizadas na aplicação 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('get_models/', views.get_models, name='get_models')
]