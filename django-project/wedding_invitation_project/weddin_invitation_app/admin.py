from django.contrib import admin
from weddin_invitation_app.models import Wedding,\
    WeddingNoneOficialEvent, WeddingOficialEvent, Guest


@admin.register(Wedding)
class WeddingAdmin:
    list_display = ('name',)


@admin.register(WeddingOficialEvent)
class WeddingOficialEventAdmin:
    list_display = ('wedding', 'date', 'address',)


@admin.register(WeddingNoneOficialEvent)
class WeddingNoneOficialEventAdmin:
    list_display = ('wedding', 'date', 'address',)


@admin.register(Guest)
class GuestAdmin:
    list_display = ('wedding', 'url_token',
                    'name', 'surname', 
                    'invitation_official_event',
                    'invitiation_none_official_event',
                    'finish_invitiation',
                    'presence_on_official_event',
                    'presence_on_none_official_event'
                    )
