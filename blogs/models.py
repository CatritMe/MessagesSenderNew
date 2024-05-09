from django.db import models

from mailing.models import NULLABLE


class Blog(models.Model):
    """Модель блога"""
    title = models.CharField(max_length=50, verbose_name='заголовок')
    text = models.TextField(verbose_name='статья')
    avatar = models.ImageField(upload_to='articles/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('title',)
