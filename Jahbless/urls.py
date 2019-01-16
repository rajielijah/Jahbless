from django.contrib import admin
from django.urls import path, include
from library import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'library'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('library/', include('library.urls')),
    path('accounts/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about_us/', views.about, name='about_us'),
    path('contact_us/', views.contact, name = 'contact_us'),
    path('search/', views.search, name='search'),
    path('lfe/', views.lfe, name='lfe'),
    path('ps/', views.ps, name='ps')
]
