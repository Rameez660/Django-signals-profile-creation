from django.forms import ModelForm
from django import forms
from .models import Profile,Description
class ProfileForm(ModelForm):
  class Meta:
    model=Profile
    fields=['bio','age','education','address','image']

class DescriptionForm(ModelForm):
  class Meta:
    model=Description
    fields=['title','desc']

# class CommentModelForm(forms.ModelForm):
#                     # forms.
#     body = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Add a comment...'}))
#     class Meta:
#         model = Comment
#         fields = ('body',)