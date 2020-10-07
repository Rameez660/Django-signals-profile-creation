from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.log_in,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.log_out,name='logout'),
    path('edit/',views.edit,name='edit'),
    path('desc/',views.desc,name='desc'),
    path('user/<int:pk>/', views.Userprofile, name='Userprofile'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("products/update/<int:myid>", views.productUpdate, name="productUpdate"),

    # path("comment/", views.comment, name="comment"),

   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
