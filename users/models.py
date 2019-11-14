from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# class User(AbstractBaseUser):
#     username=models.CharField(max_length=10,unique=True)
#     email=models.EmailField(ul('Email Address'),unique=True)
#     USERNAME_FIELD=username
#     REQUIRED_FIELDS = ['email','first_name','last_name']
#     def __str__(self):
#         return '{}'.format(self.email)
#

