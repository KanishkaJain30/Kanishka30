from django.urls import path, re_path
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.top_tweets_list, name='top_tweets_list'),
    path('tweets/', views.user_tweets_list, name='user_tweets_list'),
    path('auth/', views.auth, name='auth'),
    path('logoff/', views.sign_out, name='sign_out'),
    re_path(r'^callback/$', views.callback, name='auth_return'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('social-auth/', include('social_django.urls', namespace='social'))


]
