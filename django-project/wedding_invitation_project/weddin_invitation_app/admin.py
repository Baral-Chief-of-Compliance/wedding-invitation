from django.contrib import admin
from weddin_invitation_app.models import Wedding,\
    WeddingNoneOficialEvent, WeddingOficialEvent, Guest


admin.site.site_header = 'Приглашение на свадьбу | Админ-панель'  # Отображается вверху
admin.site.site_title = 'Приглашения на свадьбу | Админ-панель'  # Title страницы
admin.site.index_title = 'Приглашения на свадьбу | Админ-панель'  # На главной после входа

@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WeddingOficialEvent)
class WeddingOficialEventAdmin(admin.ModelAdmin):
    list_display = ('wedding', 'date', 'address',)


@admin.register(WeddingNoneOficialEvent)
class WeddingNoneOficialEventAdmin(admin.ModelAdmin):
    list_display = ('wedding', 'date', 'address',)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('wedding', 'url_token',
                    'name', 'surname', 
                    'invitation_official_event',
                    'invitiation_none_official_event',
                    'finish_invitiation',
                    'presence_on_official_event',
                    'presence_on_none_official_event',
                    'permission_plus_one',
                    'will_plus_one'
                    )
    readonly_fields = [
        'url_token',
        'will_plus_one',
        'finish_invitiation',
        'drinks',
        'music'
    ]