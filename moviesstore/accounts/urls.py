from django.urls import path
from . import views 

urlpatterns = [
    path('signup/' , views.signup, name='accounts.signup'),
    path('login/',views.loginacc, name='accounts.login'),
    path('logout/',views.logoutacc, name='accounts.logout'),
]