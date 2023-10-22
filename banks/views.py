from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from banks.serializers import BankSerializer
from banks.models import Bank


class BankAPIView(APIView):

    def get(self, request):
        try:
            ifsc = self.request.query_params.get('ifsc')
            name = self.request.query_params.get('name')
            city = self.request.query_params.get('city')

            if ifsc:
                banks = Bank.objects.filter(ifsc=ifsc)
            elif name and city:
                banks = Bank.objects.filter(name=name, city=city)
            else:
                banks = Bank.objects.all()

            serializer = BankSerializer(banks, many=True)
            return Response(serializer.data)

        except Bank.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = BankSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
