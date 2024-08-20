from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('company/<str:company_id>/', views.detailpage, name='detailpage'),
]
