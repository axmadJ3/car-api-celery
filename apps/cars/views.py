from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend


from .filters import CarFilter
from .models import Car, Make, Image
from .serializers import CarMakeSerializer, CarSerializer, ImageSerializer
from .tasks import send_email, create_car

class CarMakeListView(ListAPIView):
    queryset = Make.objects.all()
    serializer_class = CarMakeSerializer
    

class CarMakeDetailView(RetrieveAPIView):
    queryset = Make.objects.all()
    serializer_class = CarMakeSerializer
    
    
class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter    


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

@api_view(['POST'])
def CarCreateView(request):
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class MakeCreateView(CreateAPIView):
    queryset = Make.objects.all()
    serializer_class = CarMakeSerializer


class ImageView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    

@api_view(['GET'])
def EmailView(request):
    send_email.delay()
    return Response({'status': 'ok'})


@api_view(['GET'])
def car_create_task(request):
    create_car.delay()
    return Response({'status': 'ok'})