from django.urls import path
from .views import RatingCreate, RatingDetail

urlpatterns = [
    path('ratings/', RatingCreate.as_view(), name='rating-create'),
    path('ratings/<int:pk>/', RatingDetail.as_view(), name='rating-detail'),
]
