from django.urls import path
from account import views

urlpatterns = [
		path('signup/', views.signup, name = 'signup')
]