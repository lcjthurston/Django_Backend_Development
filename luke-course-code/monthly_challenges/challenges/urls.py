from django.urls import path

from . import views

# List of URLs
urlpatterns = [
    # The path function maps urls to views.
    # The angle brackets inside the quotes refer to a dynamic variable in the views.py file
    # These angled bracket views are prepeded with types that specify which view function to call.
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]