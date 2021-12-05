import app_blog
from app_blog import views
from django.conf.urls import url
app_name = " app_blog"

urlpatterns =[ 
    url(r'^posts/', views.post,name="post"),
    url(r'^home/', views.index,name="index"),
    url(r'^about/', views.about,name="about"),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.loginpageview, name="userlogin"),
    


  ]