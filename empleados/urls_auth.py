from django.urls import path
from . import views_auth

urlpatterns = [
    path('signup/', views_auth.signup, name='signup'),
    path('signin/', views_auth.signin, name='signin'),
    path('signout/', views_auth.signout, name='signout'),
]
