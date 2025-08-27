from rest_framework import serializers
from .models import Category, Job, Resume

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']

class JobSerializer(serializers.ModelSerializer):
    # Чтобы вместо ID категории отображалось её имя
    category = serializers.StringRelatedField()

    class Meta:
        model = Job
        fields = '__all__' # Включаем все поля

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'