from django.urls import path
from . import views
app_name='bankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('formpage',views.formpage,name='formpage'),
    path('logout/',views.logout,name='logout'),


]