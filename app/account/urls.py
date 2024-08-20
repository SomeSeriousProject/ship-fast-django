from django.urls import path, include
from .views import signin_with_google

app_name = "account"

urlpatterns = [
    path("google/signin/", signin_with_google, name="signin_with_google"),
]
