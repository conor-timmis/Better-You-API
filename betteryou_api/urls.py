from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home_route, logout_route

urlpatterns = [
    path('', home_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/user/', UserDetailView.as_view(), name='user-detail'),
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
