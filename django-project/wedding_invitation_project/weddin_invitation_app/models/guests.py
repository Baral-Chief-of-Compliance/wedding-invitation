import secrets

from django.db import models

from .wedding import Wedding


def generate_token() -> str:
    """Сгенерировать токен"""
    return secrets.token_urlsafe(32)


class Guest(models.Model):
    """Гость"""
    url_token = models.CharField(
        verbose_name='Уникальный токен',
        default=generate_token
    )
    wedding = models.ForeignKey(
        verbose_name='Свадьба',
        to=Wedding,
        on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name='Имя', max_length=128)
    surname = models.CharField(verbose_name='Фамилия', max_length=128)
    invitation_official_event = models.BooleanField(
        verbose_name='Приглашение на официальное мероприятие',
        default=True
    )
    invitiation_none_official_event = models.BooleanField(
        verbose_name='Приглашение на неофициальное мероприятие',
        default=True
    )
    drinks = models.TextField(
        verbose_name='Предпочтение по напиткам',
        blank=True,
        null=True
    )
    music = models.TextField(
        verbose_name='Предпочтение по музыке',
        blank=True,
        null=True
    )
    finish_invitiation = models.BooleanField(
        verbose_name='Закончил заполнение приглшения',
        default=False
    )

    presence_on_official_event = models.BooleanField(
        verbose_name='Присуствие на оф мероприятии',
        default=False
    )

    presence_on_none_official_event = models.BooleanField(
        verbose_name='Присутсвие на не оф мероприятии',
        default=False
    )

    def __str__(self) -> str:
        return f'Приглашение {self.name} {self.surname} на {self.wedding}'
    
    class Meta:
        verbose_name = 'Приглашение гостя'
        verbose_name_plural = 'Приглашение гостей'