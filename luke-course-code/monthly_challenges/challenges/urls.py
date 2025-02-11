from django.urls import path

from . import views

urlpatters = [
    path("january", views.index)
]