from rest_framework.views import APIView
from product.models import Product
from rest_framework import status
from product.api.serializers import (
    ProductSerializer
)

from django.http import JsonResponse

class ProductAPI(APIView):

      def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)



      def post(self, request, *args, **kwargs):
        form_data = request.data
        serializer = ProductSerializer(data=form_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=400)



      def put(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product, data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



      def delete(self,request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
