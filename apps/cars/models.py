from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    title = models.CharField(max_length=100, verbose_name='Категория', unique=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Make(models.Model):
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
    
    
    title = models.CharField(max_length=100, verbose_name='Производитель', unique=True)
    country = models.CharField(max_length=50, verbose_name="Страна")
    
    def __str__(self) -> str:
        return self.title
    
    
class Car(models.Model):
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        
        
    class StatusChoises:
        TRANSMISSION_CHOICES = [
        ('manual', 'Ручное'),
        ('automatic', 'Автомат'),
    ]
    
    
    make = models.ForeignKey(Make, on_delete=models.CASCADE, verbose_name='Марка', 
                             related_name='cars')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    price = models.PositiveIntegerField(verbose_name='Цена')
    transmission = models.CharField(max_length=10, verbose_name='Коробка передач', 
                                    choices=StatusChoises.TRANSMISSION_CHOICES)
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', 
                                 related_name='cars', null=True, blank=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, 
                             verbose_name='Пользователь', related_name='cars', null=True, blank=True)
    
    def __str__(self):
        return f'{self.make} {self.model}'
    

class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        

    image = models.ImageField(upload_to='cars/', verbose_name='Изображение')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина', related_name='images')

    def __str__(self) -> str:
        return self.car.model