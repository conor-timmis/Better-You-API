from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('ratings/', include('ratings.urls')),
]
