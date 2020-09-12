from django.urls import path, include
from .api.views import CoffeeMachineViewSet, CoffeePodViewSet
from rest_framework_mongoengine import routers

router = routers.DefaultRouter()

router.register('cm', CoffeeMachineViewSet, 'coffeemachine')
router.register('cp', CoffeePodViewSet, 'coffeepod')



urlpatterns = [
    path('', include(router.urls)),
]


