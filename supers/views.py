from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Supers

# Create your views here.
@api_view(['GET'])
def supers_list(request):
    supers = Supers.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)
    # return response of serializer.data returns error message
