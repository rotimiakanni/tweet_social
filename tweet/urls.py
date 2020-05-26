from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tweets', views.tweet_list_view, name="tweet_list"),
    path('createtweet', views.create_tweet_view, name="create_tweet"),
    path('tweet/<int:tweet_id>', views.tweet_view, name="index"),
]