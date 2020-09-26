from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
              # ForeignKey
  bio=models.TextField(max_length=50,null=True)
  age=models.IntegerField(null=True)
  education=models.CharField(max_length=20,null=True)
  address=models.CharField(max_length=50,null=True)
  image=models.ImageField(upload_to='media/',default='user_profile/profile.jpg')
  def __str__(self):
    return self.user.username+" profile "

class Description(models.Model):
    title=models.CharField(max_length=10000)
    desc=models.CharField(max_length=10000)

    # categorey=models.ForeignKey(Categorey,on_delete=models.CASCADE)
    # date=models.DateTimeField(auto_now_add=True)
    # thumbnail=models.ImageField(upload_to='media/')
    # video=models.FileField(upload_to='media/')
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return self.title