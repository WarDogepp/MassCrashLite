from django.db import models

class UserLocation(models.Model):


    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        app_label = 'MassCrashLite'

    def __str__(self):
        return self.name