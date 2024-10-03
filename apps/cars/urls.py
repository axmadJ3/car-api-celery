from django.urls import path

from . import views

urlpatterns = [
    path('make/', views.CarMakeListView.as_view(), name="car-make"),
    path('make/create/', views.MakeCreateView.as_view(), name="create-make"),
    path('make/<int:pk>', views.CarMakeDetailView.as_view(), name="make-detail"),
    path('car-list/', views.CarListView.as_view(), name="car-list"),
    path('car-list/create/', views.CarCreateView, name="create-car"),
    path('car-list/<int:pk>/', views.CarDetailView.as_view(), name="car-detail"),
    path('images/', views.ImageView.as_view(), name="images"),
    path('email/', views.EmailView, name="email"),
    path('car-task/', views.car_create_task, name="car-task"),
]