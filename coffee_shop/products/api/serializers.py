from rest_framework_mongoengine import serializers
from products.documents import CoffeMachine, CoffeePod

class CoffeeMachineSerializer(serializers.DocumentSerializer):

    class Meta:
        model = CoffeMachine
        fields = '__all__'

    
class CoffeePodSerializer(serializers.DocumentSerializer):
    
    class Meta:
        model = CoffeePod
        fields = '__all__'