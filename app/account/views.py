from django.shortcuts import render
from django.conf import settings
from django.urls import reverse


def signin_with_google(request):
    return render(
        request,
        "account/signin_with_google.html",
        {
            "google_client_id": settings.GOOGLE_CLIENT_ID,
            "verify_url": reverse("api:account:signin_google"),
        },
    )
