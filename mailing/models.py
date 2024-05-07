from django.db import models
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
    created_at = models.DateTimeField(auto_now_add=True)
    mail = models.ForeignKey(Mail, on_delete=models.SET_NULL, verbose_name='сообщение', **NULLABLE)
    CREATED = 'CR'
    STARTED = 'ST'
    FINISHED = 'FN'
    statuses = [(CREATED, 'создана'), (STARTED, 'запущена'), (FINISHED, 'завершена'), ]
    status = models.CharField(max_length=2, choices=statuses, default=STARTED)

    def is_upperstatus(self):
        return self.status in (self.CREATED, self.STARTED, self.FINISHED)

    def __str__(self):
        return f'{self.name} ({self.status})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

