from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    max_participants = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    meeting_point = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tour_images')

    def __str__(self):
        return self.title