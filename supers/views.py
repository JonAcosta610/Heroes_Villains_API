from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Supers
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def supers_detail(request, pk):
    try:
        supers = Supers.objects.get(pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    except Supers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)