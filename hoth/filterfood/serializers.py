from rest_framework import serializers
from .models import FilteredFood

class FilterFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredFood
        fields = ('id', 'hall', 'filters', 'foods')
