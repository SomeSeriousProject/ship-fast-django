from django.urls import path
from .views import GoogleValidateIdTokenApi

app_name = "account"

urlpatterns = [
    path(
        "signin/google/",
        GoogleValidateIdTokenApi.as_view(),
        name="signin_google",
    ),
]
