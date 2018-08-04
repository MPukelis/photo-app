from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPictureCount(models.Model):
      user = models.OneToOneField(User, on_delete=models.PROTECT)
      picture_count =  models.IntegerField(default=24)
      def __str__(self):
          # Built-in attribute of django.contrib.auth.models.User !
          return self.user.username

class UserProfileInfo(models.Model):
    def get_upload_path(instance, filename):
        return 'profile_pics/{0}/{1}'.format(instance.user.username, filename)
    # Create relationship (don't inherit from User!)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    # Add any additional attributes you want
    #portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to=get_upload_path,blank=True,)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
