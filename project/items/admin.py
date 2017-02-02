from django.contrib import admin

# Register your models here.

from .models import Car

class CarModelAdmin(admin.ModelAdmin):
	list_display 	= ['create_date', 'car_name', 'car_model']
	list_filter 	= ['car_name', 'car_model']
	search_fields 	= ['car_name', 'car_model']
	class Meta:
		model = Car

admin.site.register(Car, CarModelAdmin)