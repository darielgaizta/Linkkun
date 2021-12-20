from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<str:cred>/', views.home, name='home'),
	path('signup', views.signup, name='signup'),
	path('login', views.login, name='login'),
	path('<str:cred>/logout', views.logout, name='logout'),
	path('<str:cred>/add', views.add, name='add'),
	path('<str:cred>/delete', views.delete, name='delete'),
]