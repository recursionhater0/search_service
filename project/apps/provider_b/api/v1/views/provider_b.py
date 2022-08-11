from django.apps import apps
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from drf_spectacular.utils import extend_schema

from utils.functions import get_flights_data
from utils.serializers import ProviderSerializer


@extend_schema(responses=ProviderSerializer)
@api_view(['POST'])
def search(request: Request) -> Response:
    file_path = apps.get_app_config('provider_b').path + '/response_b.json'
    flights_data = get_flights_data(
        file_path=file_path,
        sleep_duration=60
    )
    return Response(ProviderSerializer(flights_data, many=True), status=status.HTTP_200_OK)
