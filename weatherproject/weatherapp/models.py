from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=25)
    country = models.CharField(max_length=25, default = 'United States')
    state = models.CharField(max_length=25, default = "New York")

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    def get_fields(self):
        return [self.name,self.country,self.state]
        
    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
