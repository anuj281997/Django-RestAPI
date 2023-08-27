from django.shortcuts import render
from .models import Product
from .MySerializer import ProductSerializers

from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Product_Details(APIView):
    def get_object(self,id):
        try:
            prd = Product.objects.get(id=id)            
            return prd
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        #Object recieved from database is in binary format
        try:
            prd = self.get_object(id)
            #We need to convert it into JSON, then send to client
            serializer = ProductSerializers(prd)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):  
        try:
            prd = self.get_object(id)
            prd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        prd = self.get_object(id)
        serializer = ProductSerializers(prd,data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):   
    #Fetch all records 
    def get(self,request):
        #select * from Products
        prds = Product.objects.all()
        serializer = ProductSerializers(prds,many=True)
        return Response(serializer.data)

    def post(self,request):        
        serializer = ProductSerializers(data=request.data)
        if(serializer.is_valid()):
            #Store in database
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)