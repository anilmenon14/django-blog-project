from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# Function to return back all the approved comments
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post  = models.ForeignKey('blog.Post',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_list')

class UserProfileInfo(models.Model):

    # Do not inherit class from 'User' class. Else Django will be confused about 2 User classes
    # Always use OnetoOneField like below that will map fields from this model to the User
    user = models.OneToOneField(User)

    #additional fields in Database below
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True,upload_to='profile_pics')

    def __str__(self):
        return self.user.username
