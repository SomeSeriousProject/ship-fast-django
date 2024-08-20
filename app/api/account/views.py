from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GoogleIdTokenSerializer
from .utils import verify_google_token


class GoogleValidateIdTokenApi(APIView):
    def post(self, request):
        serializer = GoogleIdTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = verify_google_token(serializer.validated_data["id_token"])
        return Response({"data": data})
