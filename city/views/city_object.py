from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from city.models import CityObjects
from city.serializers import CityObjectsSerializer, CityObjectsFullSerializer


class CityObjectsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CityObjects.objects.all()
    serializer_class = CityObjectsSerializer


class CityObjectsFullViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CityObjects.objects.all()
    serializer_class = CityObjectsFullSerializer
