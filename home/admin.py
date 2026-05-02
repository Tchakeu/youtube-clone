from django.contrib import admin

# Register your models here.


from .models import Video, Tag, Profile, Follower, Comment

admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(Comment)

