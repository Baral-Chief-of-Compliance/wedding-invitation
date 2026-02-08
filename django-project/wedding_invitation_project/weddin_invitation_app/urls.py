from django.urls import path

from weddin_invitation_app import views


urlpatterns = [
    path("thanks/", views.thanks, name='thanks'),
    path("<str:guest_token>/", views.fill_wedding, name='fill_wedding'),
]