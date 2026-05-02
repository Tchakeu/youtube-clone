from django.urls import path

from home import views
from home.views import like

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<str:pk>', views.details_video, name='video_details'),
    path('follows', views.follow, name='fol'),
    path('<uuid:video_id>/like', views.like, name='like'),
    path('<uuid:video_id>/dislike', views.dislike, name='dislike'),


]