# Generated by Django 4.2.2 on 2024-05-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_alter_mailing_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='дата первой отправки'),
        ),
        migrations.AlterField(
            model_name='mailingattempt',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='дата последней попытки'),
        ),
    ]
