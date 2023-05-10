from django.urls import path, include
from rest_framework import routers


from city.views import (
    CityObjectsViewSet,
    CityObjectsFullViewSet,
    CityObjectsByCategoryView,
    CustomCityView,
)


router = routers.DefaultRouter()

router.register("objects", CityObjectsViewSet, "objects")
router.register("objects_information", CityObjectsFullViewSet, "objects_information")
router.register("objects/city", CustomCityView, "cities")


urlpatterns = [
    path("", include(router.urls)),
    path("objects/category/<int:category_id>", CityObjectsByCategoryView.as_view()),
]
