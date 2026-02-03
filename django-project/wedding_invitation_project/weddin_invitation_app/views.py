from typing import List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
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
        'wedding_name': wedding.name
    }


    if guest.invitation_official_event:
        fields.append('presence_on_official_event')
        official_event : WeddingOficialEvent = wedding.oficial_event
        context['wedding_off_event_date'] = official_event.date
        context['wedding_off_event_address'] = official_event.address
        context['wedding_off_event_latitude'] = official_event.latitude
        context['wedding_off_event_longitude'] = official_event.longitude
        

    if guest.invitiation_none_official_event:
        fields.append('presence_on_none_official_event')
        fields.append('drinks')
        fields.append('music')
        none_official_event : WeddingNoneOficialEvent = wedding.no_oficial_event
        context['wedding_none_off_event_date'] = none_official_event.date
        context['wedding_none_off_event_address'] = none_official_event.address
        context['wedding_none_off_event_latitude'] = none_official_event.latitude
        context['wedding_none_off_event_longitude'] = none_official_event.longitude

    if guest.permission_plus_one:
        fields.append('permission_plus_one')

    GuestForm = modelform_factory(
        model=Guest,
        fields=fields,
    )

    context['form'] = GuestForm

    return render(
        request=request,
        template_name='form_for_guests.html',
        context=context
    )


