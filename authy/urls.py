from authy import views
from django.urls import path

urlpatterns = [

    path('login', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    # path('logout/', views.loggout, name='loggout'),
]