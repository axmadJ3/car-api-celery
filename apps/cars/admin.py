from django.contrib import admin

from .models import Car, Make, Image, Category


class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year']
    fields = ['make', 'model', 'year', 'color', 'price', 'transmission', 'mileage', 'description', 'category']
    list_per_page = 5
    
    
class MakeAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'country']


admin.site.register(Car, CarAdmin)
admin.site.register(Make, MakeAdmin)
admin.site.register(Image)
admin.site.register(Category)
