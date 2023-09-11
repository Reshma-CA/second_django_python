from django.urls import path
from . views import HomePage,Register,Login,logoutuser

urlpatterns = [
    path('',Register,name = 'register-page'),
    path('login/',Login,name = 'login-page'),
    path('home/', HomePage ,name = 'home-page'),
    path('logout/',logoutuser,name = 'logout'),
    
    
]
