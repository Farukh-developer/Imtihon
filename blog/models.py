from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Tour(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"
    
    
    
    
class Service(models.Model):
    country=models.CharField(max_length=200)
    destination=models.IntegerField()
    view=models.CharField(max_length=1000, null=True)
    tour=models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="tour")
    image=models.ImageField(upload_to='service_image/', null=True)
        
    def __str__(self):
        return f"{self.country}"
    
##################### Creating second one to many 

    
class Parvoz(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Yunalish(models.Model):
    avia=models.CharField(max_length=200)
    price=models.IntegerField()
    air=models.ForeignKey(Parvoz, on_delete=models.CASCADE, related_name="air")
    image_p=models.ImageField(upload_to='pathes_image/', null=True)    
    def __str__(self):
         return f"{self.avia}"
    