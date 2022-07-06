from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.models import Store, Product
from api.serializers import StoreSerializer, ProductSerializer


class StoreViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @staticmethod
    def list(request):
        stores = Store.objects.all()
        serialized_data = StoreSerializer(stores, many=True)
        return Response(serialized_data.data, status=200)

    @staticmethod
    def create(request):
        serializer = StoreSerializer(user=request.user, data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({
                'message': 'Store was created!'
            }, status=200)

        return Response({
            'message': 'Something went wrong'
        }, status=400)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
