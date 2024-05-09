# Generated by Django 4.2.2 on 2024-05-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='статья')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='Изображение')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('views_count', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
                'ordering': ('title',),
            },
        ),
    ]