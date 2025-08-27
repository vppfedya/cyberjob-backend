from django.urls import path
from .views import (
    CategoryListAPIView,
    JobListAPIView,
    JobDetailAPIView,
    ResumeListAPIView,
    ResumeDetailAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('jobs/', JobListAPIView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),
    path('resumes/', ResumeListAPIView.as_view(), name='resume-list'),
    path('resumes/<int:pk>/', ResumeDetailAPIView.as_view(), name='resume-detail'),
]