from django.urls import path
from library.views import BookList, BookDetail, AuthorList, AuthorDetail
from . import views

urlpatterns = [
    path('author/', AuthorList.as_view(), name = 'author'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name = 'author-detail'),
    path('book/', BookList.as_view(), name= 'book'),
    path('title/', views.title, name='title'),
    path('title/<int:title_id>/', views.title_detail, name='title_detail')
]