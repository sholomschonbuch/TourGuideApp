from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    duration = models.IntegerField(null=True)
    max_participants = models.IntegerField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    #meeting_point = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='tour_images')

    def __str__(self):
        return self.title