from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FormData
from .serializers import FormDataSerializer

# POST - Add
@api_view(['POST'])
def add_form_data(request):
    serializer = FormDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form data saved successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET - List
@api_view(['GET'])
def list_form_data(request):
    data = FormData.objects.all()
    serializer = FormDataSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Simulate PUT using POST
@api_view(['PUT', 'POST'])
def full_update_form_data(request, pk):
    form_data = get_object_or_404(FormData, pk=pk)
    serializer = FormDataSerializer(form_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form data fully updated", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Simulate PATCH using POST
@api_view(['PATCH', 'POST'])
def partial_update_form_data(request, pk):
    form_data = get_object_or_404(FormData, pk=pk)
    serializer = FormDataSerializer(form_data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form data partially updated", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Simulate DELETE using GET
@api_view(['DELETE', 'GET'])
def delete_form_data(request, pk):
    form_data = get_object_or_404(FormData, pk=pk)
    form_data.delete()
    return Response({"message": "Form data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
