from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Description,Commment
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
  # profile=Profile.objects.get(user=request.user)
  # descriptions=Description.objects.create(user=profile)
  # form=DescriptionForm(request.POST, request.FILES,instance=descriptions)

  # if request.method=='POST':
    
  #   if form.is_valid():
  #     form.save()
  #     # form_save = form.save(commit = False)
  #     # form_save.save(force_insert = True) 
  #     return redirect('desc')
  #   else:
  #     return HttpResponse('wrong info')

  # # if request.method=='GET':
  # #   form=DescriptionForm(instance=descriptions)

  # context={'form':form,}
  
  # return render(request,'user_profile/desc.html',context)


# =========================================================================================================================
  profile = Profile.objects.get(user=request.user)

  form=DescriptionForm()
  # post_added = False
  # profile = Profile.objects.get(user=request.user)

  if 'desc_submit' in request.POST:
    form=DescriptionForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = profile
      form.save()
      # p_form = DescriptionForm()
      # post_added = True
      return redirect('desc')
  context={'form':form,}
  return render(request,'user_profile/desc.html',context)
# =========================================================================================================================

@login_required(login_url='/login/')
def productView(request, myid):

  # Fetch the product using the id
  product = Description.objects.get(id=myid)
  # product = Description.objects.filter(id=myid)

  # For deleting post har koi apna delete krske post fb wali web se krna h
  if request.method == 'POST':
    product.delete()
    return redirect('profile')

  return render(request, 'user_profile/prodView.html', {'product':product})
                                                                # product[0]

# youtube wali web jesa kaam krna h

    #     elif 'comment' in request.POST:

    #         comment_txt=request.POST.get('comment_text')
    #         if not comment_txt.strip()=='':
    #             Commment.objects.create(comment_text=comment_txt,video=video,user=profile)
    #             return HttpResponseRedirect(f"/video/id={pk}")
    #     elif 'reply' in request.POST:
    #         comment_id=request.POST.get('comment_id')
    #         reply_text=request.POST.get('comment_reply')
    #         comment=Commment.objects.get(id=comment_id)
    #         reply=Reply.objects.create(comment=comment,user=profile,comment_text=reply_text)
    #         return HttpResponseRedirect(f"/video/id={pk}")


    # likes=Like.objects.filter(video=video).count()
    # unlikes=Unlike.objects.filter(video=video).count()
    # views=Views.objects.filter(video=video).count()
    # comments=Commment.objects.filter(video=video)
    # comp_comments=[]
    # for comment in comments:
    #     replies=Reply.objects.filter(comment=comment)
    #     c={
    #         'comment':comment,
    #         'reply':replies
    #     }
    #     comp_comments.append(c)
    # context={
    #     'video':video,
    #     'likes':likes,
    #     'unlikes':unlikes,
    #     'views':views,
    #     'related_videos':categorey_videos,
    #     'comments':comp_comments,
    #     'total_comments':comments.count()
    # }

    # return render(request, 'video_tube/video_by_id.html',context)


@login_required(login_url='/login/')
def productUpdate(request, myid):
  # For updating post
  # product = Description.objects.get(id=myid)

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