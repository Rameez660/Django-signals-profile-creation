from django.forms import ModelForm
from .models import Profile,Description
class ProfileForm(ModelForm):
  class Meta:
    model=Profile
    fields=['bio','age','education','address','image']

class DescriptionForm(ModelForm):
  class Meta:
    model=Description
    fields=['title','desc']