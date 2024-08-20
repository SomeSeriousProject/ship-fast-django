from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from account.utils import verify_google_token
from .serializers import GoogleIdTokenSerializer


class GoogleValidateIdTokenApi(APIView):
    def post(self, request):
        serializer = GoogleIdTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = verify_google_token(serializer.validated_data["id_token"])
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
            return Response({"detail": "Something went wrong"}, status=500)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"access_token": token.key})
