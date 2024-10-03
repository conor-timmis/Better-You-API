from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE
)

def clear_jwt_cookies(response):
    """
    Helper function to clear JWT authentication cookies.
    """
    cookies = [
        (JWT_AUTH_COOKIE, ''),
        (JWT_AUTH_REFRESH_COOKIE, '')
    ]
    for key, value in cookies:
        response.set_cookie(
            key=key,
            value=value,
            httponly=True,
            expires='Thu, 01 Jan 1970 00:00:00 GMT',
            max_age=0,
            samesite=JWT_AUTH_SAMESITE,
            secure=JWT_AUTH_SECURE,
        )
    return response

@api_view()
def home_route(request):
    """
    Route for home page of API.
    """
    return Response({
        "message": "Hello! This is The Better You DRF API"
    })

@api_view(['POST'])
def logout_route(request):
    """
    Route for logout of API.
    """
    response = Response({
        "message": "You have been logged out."
    })
    return clear_jwt_cookies(response)

class UserDetailView(APIView):
    """
    View to retrieve details of the authenticated user.
    """
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            data = {
                'username': user.username,
                'email': user.email,
                'date_joined': user.date_joined,
                'last_login': user.last_login,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
