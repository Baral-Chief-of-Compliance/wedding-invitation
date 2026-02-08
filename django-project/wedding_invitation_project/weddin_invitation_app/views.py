from typing import List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.forms.models import modelform_factory

from weddin_invitation_app.models import Guest, Wedding,\
WeddingNoneOficialEvent, WeddingOficialEvent


def fill_wedding(request: HttpRequest, guest_token: str) -> HttpResponse:
    """Заполнить форму"""

    guest : Guest = get_object_or_404(Guest, url_token=guest_token)
    wedding : Wedding = guest.wedding

    fields : List[str]  = []

    context = {
        'name': guest.name,
        'surname': guest.surname,
        'wedding_name': wedding.name,
        'female': guest.female,
        'male': guest.male,
        'token': guest.url_token
    }


    if guest.invitation_official_event:
        fields.append('presence_on_official_event')
        official_event : WeddingOficialEvent = wedding.oficial_event
        context['wedding_off_event_date'] = official_event.date
        context['wedding_off_event_address'] = official_event.address
        context['wedding_off_event_latitude'] = str(official_event.latitude).replace(',','.')
        context['wedding_off_event_longitude'] = str(official_event.longitude).replace(',','.')
        context['wedding_off_event_end_date'] = official_event.enddate
        

    if guest.invitiation_none_official_event:
        fields.append('presence_on_none_official_event')
        fields.append('drinks')
        fields.append('music')
        none_official_event : WeddingNoneOficialEvent = wedding.no_oficial_event
        context['wedding_none_off_event_date'] = none_official_event.date
        context['wedding_none_off_event_address'] = none_official_event.address
        context['wedding_none_off_event_latitude'] = str(none_official_event.latitude).replace(',','.')
        context['wedding_none_off_event_longitude'] = str(none_official_event.longitude).replace(',','.')
        context['wedding_none_off_event_end_date'] = none_official_event.enddate

    if guest.permission_plus_one:
        fields.append('will_plus_one')

    GuestForm = modelform_factory(
        model=Guest,
        fields=fields,
    )

    context['form'] = GuestForm


    # Отображение материала, если гость уже завершил 
    # заявку
    if guest.finish_invitiation:
        context.pop('form')
        return render(
            request=request,
            template_name='info.html',
            context=context
        )


    # Обработку POST запроса
    if request.method == 'POST':

        form = GuestForm(request.POST)
        if form.is_valid():
            guest : Guest = get_object_or_404(Guest, url_token=guest_token)
            update_fields = []
            form_keys = form.cleaned_data.keys()

            if 'presence_on_official_event' in form_keys:
                guest.presence_on_official_event = form.cleaned_data['presence_on_official_event']
                update_fields.append('presence_on_official_event')

            if 'presence_on_none_official_event' in form_keys:
                guest.presence_on_none_official_event = form.cleaned_data['presence_on_none_official_event']
                update_fields.append('presence_on_none_official_event')

            if 'drinks' in form_keys:
                guest.drinks = form.cleaned_data['drinks']
                update_fields.append('drinks')

            if 'music' in form_keys:
                guest.music = form.cleaned_data['music']
                update_fields.append('music')

            if 'will_plus_one' in form_keys:
                guest.will_plus_one = form.cleaned_data['will_plus_one']
                update_fields.append('will_plus_one')
            
            guest.finish_invitiation = True
            update_fields.append('finish_invitiation')

            guest.save(update_fields=update_fields)
            return redirect('thanks')


    return render(
        request=request,
        template_name='form_for_guests.html',
        context=context
    )


def thanks(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name='finish.html'
    )


def error_404(request, exception):
    """Страница ошибки Не найдено"""
    return render(
        request=request,
        template_name='404.html',
        status=404
    )


def error_500(request):
    """Страницы серверной ошибки"""
    return render(
        request=request,
        template_name='500.html',
        status=500
    )


def error_403(request, exception):
    """Доступ запрещен"""
    return render(
        request=request,
        template_name='403.html',
        status=403
    )


def error_400(request, exception):
    """Плохой запрос"""
    return render(
        request=request,
        template_name='400.html',
        status=400
    )
