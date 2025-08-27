from django.db import models
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    icon = models.CharField(max_length=20, blank=True, null=True, verbose_name="Иконка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    company = models.CharField(max_length=255, verbose_name="Компания")
    location = models.CharField(max_length=255, verbose_name="Локация")
    job_type = models.CharField(max_length=50, verbose_name="Тип занятости")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="jobs", verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")
    requirements = ArrayField(models.CharField(max_length=200), verbose_name="Требования")
    salary = models.CharField(max_length=100, blank=True, null=True, verbose_name="Зарплата")
    posted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-posted_at']

class Resume(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя соискателя")
    position = models.CharField(max_length=255, verbose_name="Должность")
    location = models.CharField(max_length=255, verbose_name="Локация")
    experience = models.CharField(max_length=100, verbose_name="Опыт")
    skills = ArrayField(models.CharField(max_length=200), verbose_name="Навыки")
    description = models.TextField(verbose_name="О себе")
    contact = models.CharField(max_length=255, verbose_name="Контакт (telegram/email)")
    posted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        ordering = ['-posted_at']