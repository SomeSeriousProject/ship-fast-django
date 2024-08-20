from django.http import JsonResponse


def index(request):
    return JsonResponse({"detail": "API is working"})
