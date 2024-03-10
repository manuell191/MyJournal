from . import views
from django.urls import path

urlpatterns = [
	path('', views.index, name='home'),
	path('login/', views.userLogin, name='login'),
	path('signup/', views.signup, name='signup'),
	path('load/', views.load, name='load'),
	path('post/', views.createPost, name='post'),
	path('view/', views.viewPost, name='view')
]