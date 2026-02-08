from django.db import models

class Wedding(models.Model):
    """Модель свадьбы"""
    name = models.CharField(verbose_name='Наименование свадьбы', max_length=128)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Свадьба'
        verbose_name_plural = 'Свадьбы'


class WeddingOficialEvent(models.Model):
    """Официальное мероприятие в загсе"""
    wedding = models.OneToOneField(
        verbose_name='Свадьба',
        to=Wedding,
        on_delete=models.CASCADE,
        related_name='oficial_event'
    )
    date = models.DateTimeField(verbose_name='Дата и время мероприятия')
    enddate = models.DateTimeField(verbose_name='Дата и время окончания мероприятия', null=True, blank=True)
    address = models.TextField(verbose_name='Адрес мероприятия')
    latitude = models.FloatField(verbose_name='Ширина')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self) -> str:
        return f'Официальное мероприятие {self.wedding}'
    
    class Meta:
        verbose_name = 'Официальное мероприятие'
        verbose_name_plural = 'Официальные мероприятия'


class WeddingNoneOficialEvent(models.Model):
    """Не официальное мероприятия"""
    wedding = models.OneToOneField(
        verbose_name='Свадьба',
        to=Wedding,
        on_delete=models.CASCADE,
        related_name='no_oficial_event',
    )
    date = models.DateTimeField(verbose_name='Дата и вермя мероприятия')
    enddate = models.DateTimeField(verbose_name='Дата и время окончания мероприятия', null=True, blank=True)
    address = models.TextField(verbose_name='Адрес мероприятия')
    latitude = models.FloatField(verbose_name='Ширина')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self) -> str:
        return f'Неофициальное мероприятие {self.wedding}'
    
    class Meta:
        verbose_name = 'Не официальное мероприятие'
        verbose_name_plural = 'Не официальные мероприятия'
