from django_filters import rest_framework as filters


from .models import Car


class CarFilter(filters.FilterSet):
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    year_gte = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_lte = filters.NumberFilter(field_name='year', lookup_expr='lte')
    make = filters.CharFilter(field_name='make', lookup_expr='icontains')
    transmission = filters.ChoiceFilter(field_name='transmission', choices=Car.StatusChoises.TRANSMISSION_CHOICES)
    
    class Meta:
        model = Car
        fields = ['make', 
                  'model', 
                  'price_gte', 
                  'price_lte', 
                  'transmission', 
                  'year_gte', 
                  'year_lte'
                  ]
        