from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='login'),
    path('logout/',views.signout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('editinfo/',views.editinfo,name='editinfo'),
    path('changepassword/',views.changepassword,name='changepassword')
]

