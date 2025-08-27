from rest_framework import generics
from .models import Category, Job, Resume
from .serializers import CategorySerializer, JobSerializer, ResumeSerializer

# Представление для получения списка всех категорий
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Представление для получения списка всех активных вакансий
class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer

# Представление для получения одной конкретной вакансии
class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer

# Представление для получения списка всех активных резюме
class ResumeListAPIView(generics.ListAPIView):
    queryset = Resume.objects.filter(is_active=True)
    serializer_class = ResumeSerializer

# Представление для получения одного конкретного резюме
class ResumeDetailAPIView(generics.RetrieveAPIView):
    queryset = Resume.objects.filter(is_active=True)
    serializer_class = ResumeSerializer