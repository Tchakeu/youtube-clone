import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')

    def __str__(self):
        return self.title


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="tags")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    media = models.FileField(upload_to="media/videos/%y")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("video-detail", args=[str(self.id)])


class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    video = models.ForeignKey("home.Video", on_delete=models.CASCADE, related_name="notification_post", null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_from_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_to_user")
    notification_types = models.IntegerField(choices=NOTIFICATION_TYPES, null=True, blank=True)
    text_preview = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video.name


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_likes")

    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        video = like.video
        sender = like.user
        notify = Notification(video=video, sender=sender, user=video.user)
        notify.save()

    def user_unliked_post(sender, instance, *args, **kwargs):
        like = instance
        video = like.video
        sender = like.user
        notify = Notification.objects.filter(video=video, sender=sender, notification_types=1)
        notify.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profiles/profile",
                                    default='media/blank-profile-picture.png')

    def __str__(self):
        return str(self.user)


class Follower(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

