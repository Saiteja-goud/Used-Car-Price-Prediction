from django.db import models

class PredictionRecord(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    mileage = models.FloatField()
    engine_size = models.FloatField()
    horsepower = models.FloatField()
    predicted_price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.predicted_price}"
