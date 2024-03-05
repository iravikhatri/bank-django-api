from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from banks.serializers import BankSerializer
from banks.models import Bank


class BankListAPIView(APIView):

    def get(self, request):
        try:
            ifsc, name, city = (request.query_params.get(param) \
                for param in ['ifsc', 'name', 'city'])

            # Define initial queryset
            queryset = Bank.objects.all()
            if name:
                queryset = queryset.filter(name=name)
            if city:
                queryset = queryset.filter(city=city)
            if ifsc:
                queryset = queryset.filter(ifsc=ifsc)

            serializer = BankSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Bank.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankDetailAPIView(APIView):

    def get(self, request, pk=None, format=None):
        try:
            bank_object = Bank.objects.get(pk=pk)
            serializer = BankSerializer(bank_object)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Bank.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def patch(self, request, pk=None, format=None):
        bank_object = Bank.objects.get(pk=pk)
        serializer = BankSerializer(instance=bank_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None, format=None):
        try:
            bank_object = Bank.objects.get(pk=pk)
            bank_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Bank.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
