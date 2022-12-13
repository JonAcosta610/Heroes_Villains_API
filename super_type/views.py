from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import SuperType
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
