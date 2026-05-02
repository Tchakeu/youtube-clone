from django.urls import path

from profiles import views
from home.views import like

urlpatterns = [
    path('profile/<str:id_user>', views.profile),


]