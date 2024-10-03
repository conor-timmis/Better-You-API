from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home_route, logout_route, UserDetailView

urlpatterns = [
    path('', home_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/logout/', logout_route),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/dj-rest-auth/user/', UserDetailView.as_view(), name='user-detail'),
    path('api/profiles/', include('profiles.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/followers/', include('followers.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
