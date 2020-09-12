from django.http import JsonResponse
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CoffeePodSerializer, CoffeeMachineSerializer
from products.documents import CoffeePod, CoffeMachine

class CoffeeMachineViewSet(ModelViewSet):

    serializer_class = CoffeeMachineSerializer
    queryset = CoffeMachine.objects
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        params = self.request.GET
        
        type_ = params.get('type_')
        water_line = params.get('wl')

        if params:
            query = {}

            if  type_:
                query['type_'] = type_

            if water_line:
                query['water_compatible'] = True if water_line == 'yes' else False

            queryset = queryset.filter(**query)
        
        serialized_queryset = CoffeeMachineSerializer(queryset, many=True)

        return Response(serialized_queryset.data)


class CoffeePodViewSet(ModelViewSet):

    serializer_class = CoffeePodSerializer
    queryset = CoffeePod.objects
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        params = self.request.GET
    
        flavor = params.get('flavor')
        size = params.get('size')
        type_ = params.get('type_')

        if params:
            query = {}
            
            if  type_:
                query['type_'] = type_

            if  flavor:
                query['flavor'] = flavor

            if size:
                query['dozen_count'] = size

            queryset = queryset.filter(**query)
        
        serialized_queryset = CoffeePodSerializer(queryset, many=True)

        return Response(serialized_queryset.data)

        

        


