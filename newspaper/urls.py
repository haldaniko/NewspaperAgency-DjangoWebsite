from django.urls import path, include
from newspaper.views import index

app_name = "newspaper"


urlpatterns = [
    path("", index, name="index"),
]
