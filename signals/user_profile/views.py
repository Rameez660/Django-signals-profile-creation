from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Description
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,DescriptionForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
  descriptions=Description.objects.all()

# Home page me without login jane ka code

  user=User.objects.get(id=request.user.id)
  if not Profile.objects.filter(user=user):
    Profile.objects.create(user=user)

# ===========================================

  return render(request,'user_profile/index.html',{'descriptions':descriptions})

@login_required(login_url='/')
def profile(request):
  # user=request.user
  # user=User.objects.get(id=user)
  profile=Profile.objects.get(user=request.user)
  # description=Description.objects.filter(user=profile)
  descriptions=Description.objects.filter(user=profile)
  description_info = []
  for desc in descriptions:
    description = {'description': desc}
    
    description_info.append(description) 


  # p=Profile.objects.get(user=request.user)
  context={
    'profile':profile,'description':description_info,
  }  
  return render(request,'user_profile/profile.html',context)


@login_required(login_url='/login')
def edit(request):
  user=Profile.objects.get(user=request.user)

  if request.method=='GET':
    form=ProfileForm(instance=user)
    context={
      'form':form,
    }
    return render(request,'user_profile/edit.html',context)
  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES,instance=user)
    if form.is_valid():
      form.save()
      return redirect('/profile')
    else:
      return HttpResponse('not changed the profile')  


@login_required(login_url='/login')
def desc(request):
  profile=Profile.objects.get(user=request.user)
  descriptions=Description.objects.create(user=profile)
  form=DescriptionForm(request.POST or None, request.FILES or None,instance=descriptions)  

  if request.method=='POST':
    
    if form.is_valid():
      form.save()
      form_save = form.save(commit = False)
      form_save.save(force_insert = True) 
      return redirect('desc')
    else:
      return HttpResponse('wrong info')

  # if request.method=='GET':
  #   form=DescriptionForm(instance=descriptions)

  context={'form':form,}
  
  return render(request,'user_profile/desc.html',context)

@login_required(login_url='/login/')
def productView(request, myid):

  # Fetch the product using the id
  product = Description.objects.get(id=myid)
  # product = Description.objects.filter(id=myid)

  # For deleting post
  if request.method == 'POST':
    product.delete()
    return redirect('profile')

  return render(request, 'user_profile/prodView.html', {'product':product})
                                                                # product[0]

@login_required(login_url='/login/')
def productUpdate(request, myid):
  # For updating post
  product = Description.objects.get(id=myid)

  form = DescriptionForm(instance=product)

  if request.method == 'POST':
    form = DescriptionForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      return redirect('ProductView',myid=myid)

  context = {'form':form}
  return render(request, 'user_profile/productUpdate.html', context)

@login_required(login_url='/login/')
def Userprofile(request,pk):
    profile=Profile.objects.get(id=pk)
    description=Description.objects.filter(user=profile)
    description_info = []
    for desc in description:
        description = {
            'description': desc,
        }
        description_info.append(description)
    context={
        'description':description_info,
        'user':profile,

    }
    return render(request,'user_profile/user_profile.html',context)


def log_in(request):
  if request.method=='GET':
    return render(request,'user_profile/login.html')
  elif request.method=='POST':
    user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
    print(user)
    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      return redirect('/login')

def signup(request):
  if request.user.is_authenticated:
      return redirect('/')
  else:
    if request.method=='GET':
      context={
        'form':UserCreationForm()
      }
      return render(request,'user_profile/signup.html',context)
    elif request.method=='POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/login')
      else:
        return redirect('/signup')

@login_required(login_url='/login')
def log_out(request):
  logout(request)
  return redirect('login')
                    # / 