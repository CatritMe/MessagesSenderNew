# Generated by Django 4.2.2 on 2024-05-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0010_mailing_sent_time_alter_mailing_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('создана', 'создана'), ('запущена', 'запущена'), ('завершена', 'завершена')], default='создана', max_length=9),
        ),
    ]