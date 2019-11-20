from rest_framework import serializers
from bank_branches.models import Banks

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'
