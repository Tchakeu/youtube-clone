from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from home.models import Profile, Video, Likes


# Create your views here.

def register(request):

    return render(request, 'authy/signup.html', )


def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(username, email, password)
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request, my_user)
                return redirect('/')
            return redirect('/loginn')


    except:
        invalid = "User already exists"
        return render(request, 'authy/signup.html', {'invalid': invalid})

    return render(request, 'authy/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        userr = authenticate(request, username=username, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/')

        invalid = "Information Invalide "
        return render(request, 'authy/signin.html', {'invalid': invalid})

    return render(request, 'authy/signin.html')



def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        video = get_object_or_404(Video, id=id)

        like_filter = Likes.objects.filter(post_id=id, username=username).first()

        if like_filter is None:
            new_like = Likes.objects.create(post_id=id, username=username)
            video.no_of_likes = video.no_of_likes + 1
        else:
            like_filter.delete()
            video.no_of_likes = video.no_of_likes - 1

        video.save()

        # Generate the URL for the current post's detail page
        print(video.id)

        # Redirect back to the post's detail page
        return redirect('/#'+id)

