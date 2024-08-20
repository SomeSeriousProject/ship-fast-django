from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model, login
from .utils import verify_google_token


def signin_with_google(request):
    return render(
        request,
        "account/signin_with_google.html",
        {
            "google_client_id": settings.GOOGLE_CLIENT_ID,
            "verify_url": reverse("account:signin_with_google_confirm"),
        },
    )


def signin_with_google_confirm(request):
    try:
        id_token = request.GET.get("id_token")
        if not id_token:
            return HttpResponse("id_token is required!")

        data = verify_google_token(id_token)
        email: str = data["email"]
        user = None

        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create_user(
                username=email.split("@")[0],
                email=email,
            )

        if not user:
            return HttpResponse("Something went wrong. Please contact the webmaster.")

        login(request=request, user=user)
        return JsonResponse({"url": reverse("account:signin_with_google")})
    except:
        return HttpResponse("Something went wrong. Please contact the webmaster.")
