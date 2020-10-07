from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
              # ForeignKey
  bio=models.TextField(max_length=50,default='Your Bio')
  age=models.IntegerField(default='00')
  education=models.CharField(max_length=20, default='Your Education')
  address=models.CharField(max_length=50, default='Your Address')
  image=models.ImageField(upload_to='media/',default='profile.jpg')
  def __str__(self):
    return self.user.username+" profile "

class Description(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
                
    title=models.CharField(max_length=10000)
    desc=models.CharField(max_length=10000)

    # categorey=models.ForeignKey(Categorey,on_delete=models.CASCADE)
    # date=models.DateTimeField(auto_now_add=True)
    # thumbnail=models.ImageField(upload_to='media/')
    # video=models.FileField(upload_to='media/')

    def __str__(self):
        return self.title


class Commment(models.Model):
    comment_text=models.TextField(max_length=200)
    # date=models.DateTimeField(auto_now_add=True)
    description=models.ForeignKey(Description,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text
    class Meta:
        verbose_name='Comment'
        verbose_name_plural='Comments'