from django.urls import path

from seven.views import calculate

app_name = "seven"

urlpatterns = [path("", view=calculate, name="index")]
