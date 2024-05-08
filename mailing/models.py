
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """модель клиента для отправки рассылок"""
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(max_length=50, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mail(models.Model):
    """Модель сообщения для рассылки"""
    topic = models.CharField(max_length=50, verbose_name='тема')
    text = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Mailing(models.Model):
    """модель рассылки"""
    name = models.CharField(max_length=50, verbose_name='название')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания рассылки')
    sent_time = models.DateField(default=timezone.now, verbose_name='время отправки рассылки', **NULLABLE)
    mail = models.ForeignKey(Mail, on_delete=models.SET_NULL, verbose_name='сообщение', **NULLABLE)
    CREATED = 'создана'
    STARTED = 'запущена'
    FINISHED = 'завершена'
    statuses = [(CREATED, 'создана'), (STARTED, 'запущена'), (FINISHED, 'завершена'), ]
    status = models.CharField(max_length=9, choices=statuses, default=CREATED)
    DAY = 'DY'
    WEEK = 'WK'
    MONTH = 'MN'
    periods = [(DAY, 'раз в день'), (WEEK, 'раз в неделю'), (MONTH, 'раз в месяц'), ]
    periodicity = models.CharField(max_length=2, choices=periods, default=MONTH)
    client = models.ManyToManyField(Client, verbose_name='получатели')

    # def is_upperstatus(self):
    #     return self.status in (self.CREATED, self.STARTED, self.FINISHED)

    def __str__(self):
        return f'{self.name} ({self.status})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingAttempt(models.Model):
    """Модель для попыток рассылки"""
    updated_at = models.DateField(auto_now=True, verbose_name='дата последней попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='в рассылке')
    is_success = models.BooleanField(default=True, verbose_name='успешно')
    answer = models.TextField(verbose_name='ответ почтового сервера')

    def __str__(self):
        return self.is_success

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'



