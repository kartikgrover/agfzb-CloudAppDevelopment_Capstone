from django.db import models
from django.utils.timezone import now


from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    dealer_id = models.CharField(max_length=100)  # Assuming the dealer ID is a string
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name):
        self.id = id
        self.city = city
        self.state = state
        self.st = st
        self.address = address
        self.zip = zip
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.full_name = full_name

    def __str__(self):
        return self.full_name  # Return the full name as the string representation for CarDealer


    def __str__(self):
        return "Dealer name: " + self.full_name




# <HINT> Create a plain Python class `DealerReview` to hold review data
