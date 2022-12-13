from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperTypeSerializer
from .models import SuperType
from rest_framework import status
# from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def type_list(request):
    type = SuperType.objects.all()
    serializer = SuperTypeSerializer(type, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def type_detail(request, pk):
    try:
        type = SuperType.objects.get(pk=pk)
        serializer = SuperTypeSerializer(type)
        return Response(serializer.data)
    except SuperType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)