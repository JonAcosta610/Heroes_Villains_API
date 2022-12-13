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
        print(super_type)

        supers = Supers.objects.all()

        if super_type:
            supers = supers.filter(type__type=super_type)

        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
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
        if super_type:
            queryset = queryset.filter(super_type=super_type)
        serializer = SuperSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        Supers.delete
        return Response(status=status.HTTP_204_NO_CONTENT)