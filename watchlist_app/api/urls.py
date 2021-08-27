from django.urls import path

from .views import *

urlpatterns = [
    path('list/', WatchListListView.as_view(), name='watchlist-list'),
    path('list/<int:pk>/', WatchListDetailView.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformListView.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name='stream-list'),
]
