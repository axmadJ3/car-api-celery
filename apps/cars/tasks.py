# myapp/tasks.py
from django.core.mail import send_mail
from celery import shared_task
from time import sleep

import random

from .models import Car, Make, Category
from apps.accounts.models import CustomUser

@shared_task
def send_email():
    send_mail('Test mail', 'This is test mail', 'utubahmad031@gmail.com', 
              ['utubahmad031@gmail.com'], fail_silently=False)
    return 'ok'


@shared_task
def create_car():
    category = Category.objects.get(id=2)  
    make = Make.objects.get(id=1)  
    user = CustomUser.objects.get(phone_number='998500781179')
    for _ in range(1, 3):  
        car = Car.objects.create(
            make=make,  
            model=str(random.randint(1000, 100000)),
            year=random.randint(1900, 2024),  
            color=random.choice(['red', 'green', 'blue', 'black', 'white']),  
            price=random.randint(10000000, 100000000),  
            transmission=random.choice(['manual', 'automatic']),  
            mileage=random.randint(10000, 100000), 
            description=f'Random description 1{_} - {random.randint(10, 100)}', 
            category=category,  
            user=user 
        )
    return 'ok'
