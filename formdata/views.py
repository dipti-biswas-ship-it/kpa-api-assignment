from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FormData
from .serializers import FormDataSerializer

@api_view(['POST'])
def add_form_data(request):
    serializer = FormDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form data saved successfully", "data":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_form_data(request):
    data = FormData.objects.all()
    serializer = FormDataSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)