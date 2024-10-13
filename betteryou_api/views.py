from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE
)

def clear_jwt_cookies(response):
    """ Helper function to clear JWT authentication cookies. """
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
    """ Route for home page of API. """
    return Response({
        "message": "Hello! This is The Better You DRF API"
    })

@api_view(['POST'])
def logout_route(request):
    """ Route for logout of API. """
    response = Response({
        "message": "You have been logged out."
    })
    return clear_jwt_cookies(response)

class UserDetailView(APIView):
    """ View to retrieve details of the authenticated user. """
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

class TokenRefreshView(APIView):
    """ View to handle token refresh. """
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'Refresh token is missing'}, status=400)

            token = RefreshToken(refresh_token)
            new_token = {
                'access': str(token.access_token)
            }
            return Response(new_token, status=200)
        except Exception as e:
            return Response({'error': 'Server Error'}, status=500)
