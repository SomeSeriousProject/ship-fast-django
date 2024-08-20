from django.urls import path, include
from .views import index

app_name = "api"

urlpatterns = [
    path("account/", include("api.account.urls")),
    path("", index, name="index"),
]
