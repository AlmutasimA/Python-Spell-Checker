from django.urls import path
from . import views

urlpatterns = [
  path("suggest/", views.suggest_corrections, name="suggest_corrections"),
  path("add/", views.add_to_dictionary, name="add_to_dictionary"),
]