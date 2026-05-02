from django.contrib.auth.models import User
from django.shortcuts import render

from home.models import Profile, Video, Follower


# Create your views here.

def profile(request, id_user):
    user_object = User.objects.get(username=id_user)
    profile = Profile.objects.get(user=request.user)
    all_profiles = Profile.objects.all()
    user_profile = Profile.objects.get(user=user_object)
    user_videos = Video.objects.filter(name=id_user)
    video_all = Video.objects.all()
    user_video_length = len(user_videos)
    print(id_user)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_videos': user_videos,
        'user_video_length': user_video_length,
        'profile': profile,
        'video_all': video_all,
        'all_profiles': all_profiles,

    }
    return render(request, 'profiles/profile.html', context)
