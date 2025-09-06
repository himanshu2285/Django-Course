from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    
    
    

    
class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name + " " + str(self.speed)
    