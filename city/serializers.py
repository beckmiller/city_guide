from rest_framework import serializers

from city.models import CityObjects, Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"


class CityObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityObjects
        fields = ("name",)


class CityObjectsFullSerializer(serializers.ModelSerializer):
    category_object = serializers.CharField(source="category")
    location_city = serializers.CharField(source="city")

    class Meta:
        model = CityObjects
        fields = (
            "name",
            "description",
            "address",
            "address_number",
            "contact",
            "category_object",
            "location_city",
        )
