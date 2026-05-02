from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import json
import time
from django.core.serializers.json import DjangoJSONEncoder

from home.forms import CommentForm
from home.models import Video, Profile, Likes, Follower, Tag, Comment


# Create your views here.

def index(request):
    global name
    video = Video.objects.all()
    tag = Tag.objects.all()
    profiles = Profile.objects.all()
    profile = Profile.objects.get(user=request.user)
    abonne = Follower.objects.filter(follower=request.user)
    unique_abonne = set(abonne)

    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            video = Video.objects.filter(name__icontains=name)

            if request.method == "GET":
                name = request.GET.get('recherche')
                if name is not None:
                    video = Video.objects.filter(name__icontains=name)

    context = {
        'video': video,
        'tag': tag,
        'profile': profile,
        'profiles': profiles,
        'abonne': abonne,
        'unique_abonne': unique_abonne,

    }
    if ((request.method == "GET") and (name is not None)):
        return render(request, 'home/search.html', context)
    else:
        return render(request, 'home/home.html', context)


def details_video(request, pk):
    video = Video.objects.get(id=pk)
    comments = Comment.objects.filter(video=video.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.video = video
            new_comment.save()
    else:
        comment_form = CommentForm()
    user_videos = Video.objects.filter(author=request.user)
    user_video_length = len(user_videos)
    x = Follower.objects.filter(user=video.author)
    nbre_abonne = len(x)
    profile = Profile.objects.get(user=request.user)
    videos = Video.objects.all()

    follower = request.user.username
    user = request.user
    if Follower.objects.filter(follower=follower, user=user).first():
        follow_unfollow = 'Unfollow'
    else:
        follow_unfollow = 'S`abonner'
    user_followers = len(Follower.objects.filter(user=request.user))
    user_following = len(Follower.objects.filter(follower=request.user))

    context = {
        'video': video,
        'all_video': videos,
        'profile': profile,
        'follow_unfollow': follow_unfollow,
        'user_following': user_following,
        'user_followers': user_followers,
        'user_video_length': user_video_length,
        'nbre_abonne': nbre_abonne,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'home/details_videos.html', context)


def like(request, video_id):
    user = request.user
    video = Video.objects.get(id=video_id)
    current_likes = video.likes
    liked = Likes.objects.filter(user=user, video=video).count()

    if not liked:
        Likes.objects.create(user=user, video=video)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, video=video).delete()
        current_likes = current_likes - 1

    video.likes = current_likes
    video.save()

    return HttpResponseRedirect(reverse('video_details', args=[video_id]))


def dislike(request, video_id):
    user = request.user
    video = Video.objects.get(id=video_id)
    current_likes = video.dislikes
    liked = Likes.objects.filter(user=user, video=video).count()

    if not liked:
        Likes.objects.create(user=user, video=video)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, video=video).delete()
        current_likes = current_likes - 1

    video.dislikes = current_likes
    video.save()

    return HttpResponseRedirect(reverse('video_details', args=[video_id]))


def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Follower.objects.filter(follower=follower, user=user).first():
            delete_follower = Follower.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/')
        else:
            new_follower = Follower.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/')
    else:
        return redirect('/')





