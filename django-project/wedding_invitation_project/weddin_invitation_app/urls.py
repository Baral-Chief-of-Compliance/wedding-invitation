from django.urls import path

from weddin_invitation_app import views


urlpatterns = [
    path("<str:guest_token>/", views.fill_wedding, name='fill_wedding')
]