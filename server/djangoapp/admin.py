from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel to be used within CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel

# Customizing CarModelAdmin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'dealer_id')  # Define the fields to display in the list
    # Add more customizations as required

# Customizing CarMakeAdmin with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Embed CarModelInline within CarMake admin
    list_display = ('name', 'description')  # Fields to display in the list
    # Add more customizations as needed

# Registering models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
