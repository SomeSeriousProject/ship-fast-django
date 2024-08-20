from django.urls import path, include
from .views import signin_with_google, signin_with_google_confirm

app_name = "account"

urlpatterns = [
    path("google/signin/", signin_with_google, name="signin_with_google"),
    path(
        "google/signin/confirm/",
        signin_with_google_confirm,
        name="signin_with_google_confirm",
    ),
]
