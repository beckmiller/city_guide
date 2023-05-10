from rest_framework import generics
from city.models import CityObjects
from city.serializers import CityObjectsFullSerializer


class CityObjectsByCategoryView(generics.ListAPIView):
    serializer_class = CityObjectsFullSerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return CityObjects.objects.filter(category=category_id)
