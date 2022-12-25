from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Supers
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('type')

        queryset = Supers.objects.all()

        if super_type:
            queryset = queryset.filter(type__type=super_type)
            serializer = SuperSerializer(queryset, many=True)
            return Response(serializer.data)

        heroes = queryset.filter(type__type='Hero')
        villains = queryset.filter(type__type='Villain')
        hero_serializer = SuperSerializer(heroes, many=True)
        villain_serializer = SuperSerializer(villains, many=True)


        custom_response_dict = {
            'Hero': hero_serializer.data,
            'Villain': villain_serializer.data
        }
        return Response(custom_response_dict)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        try:
            supers = Supers.objects.get(pk=pk)
            serializer = SuperSerializer(supers)
            return Response(serializer.data)
        except Supers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        Supers.delete
        return Response(status=status.HTTP_204_NO_CONTENT)