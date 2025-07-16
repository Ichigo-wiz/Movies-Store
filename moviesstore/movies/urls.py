from django.urls import path 
from movies import views

urlpatterns = [
    path('',views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create', views.create_review, name='movies.create_review')
]