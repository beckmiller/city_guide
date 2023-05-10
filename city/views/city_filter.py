from rest_framework import generics
from city.models import CityObjects
from city.serializers import CityObjectsFullSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class ObjectsByCityView(generics.ListAPIView):
    serializer_class = CityObjectsFullSerializer

    def get_queryset(self):
        city_id = self.kwargs["city_id"]
        return CityObjects.objects.filter(city=city_id)


class CustomCityView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = CityObjects.objects.all()
    serializer_class = CityObjectsFullSerializer

    @action(methods=["get"], detail=True)
    def city(self, request):
        city_id = self.kwargs["city_id"]
        queryset = CityObjects.objects.filter(city=city_id)
        return Response(queryset)
