from django.urls import path

from weddin_invitation_app import views


urlpatterns = [
    path("", views.fill_wedding, name='fill_wedding')
]