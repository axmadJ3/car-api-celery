from rest_framework import serializers

from .models import Car, Make, Image


class CarMakeSerializer(serializers.ModelSerializer):
    car_count = serializers.SerializerMethodField()
    all_cars = serializers.SerializerMethodField()
    
    def get_car_count(self, instance):
        return instance.cars.all().count()
    
    def get_all_cars(self, instance):
        return CarSerializer(instance.cars.all(), many=True).data
    
    class Meta:
        model = Make
        fields = '__all__'
            
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        