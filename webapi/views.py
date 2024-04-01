from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from grandeur.models import Grandeur,Mesure
from .serializers import GrandeurSerializer,MesureSerializer
# Create your views here.

@api_view(['GET','POST'])
def add_list_grandeur(request):
    if request.method=='GET':
        #get grandeur list
        grandeurs=Grandeur.objects.all()
        serializer=GrandeurSerializer(grandeurs,many=true)
        return Response(serializer.data)
    elif request.method=='POST':
        #add grandeur
        serializer=GrandeurSerializer(data=request.data)
        if serializer.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def get_modif_delete_grandeur(request,pk):
    try:
        grandeur=Grandeur.objects.get(pk=pk)
    except Grandeur.DoesNotExists:
        return Response(status=status.HTTP_400_NOT_FOUND)
    if request.method=='GET':
        serializer=GrandeurSerialzer(grandeur)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=GrandeurSerialzer(grandeur,request.data)
        if(serializer.is_valid()):
            serialzer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        grandeur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)