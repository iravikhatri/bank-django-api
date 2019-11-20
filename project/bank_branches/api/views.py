from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from bank_branches.api.serializers import BanksSerializer

from bank_branches.models import Banks

class BanksApiView(APIView):
    def get(self, request):
        try:
            ifsc = self.request.query_params.get('ifsc')
            bank_name = self.request.query_params.get('bank_name')
            city = self.request.query_params.get('city')

            if ifsc:
                banks = Banks.objects.filter(ifsc=ifsc)
            elif bank_name and city:
                banks = Banks.objects.filter(bank_name=bank_name, city=city)
            else:
                banks = Banks.objects.all()

            all_banks = []
            for bank in banks:
                serializer = BanksSerializer(bank)
                print(serializer.data)
                all_banks.append(serializer.data)
            return Response(all_banks)
        except Banks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        serializer = BanksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
