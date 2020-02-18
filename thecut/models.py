from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    car_model = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.car_model

    def get_absolute_url(self):
        return "/%i/" % self.pk
        
            
class Manufacturer(models.Model): 
    name = models.CharField(max_length=40, default='')
    description = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name + ',' + self.description