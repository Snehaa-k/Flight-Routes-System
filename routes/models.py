from django.db import models
from django.db import models

# Create your models here.

class Airport(models.Model):
    """
    Model representing an airport with a unique code.
    """
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.code


class Route(models.Model):
    """
    Represents a flight route between two airports.
    Attributes:
        source (Airport): The departure airport.
        destination (Airport): The arrival airport.
        position (str): The position of the route ('left' or 'right').
        duration (int): Duration in minutes or distance in kilometers.
    """
    POSITION_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="source_routes")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination_routes")
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes or distance in km")

    def __str__(self):
        return f"{self.source} -> {self.destination} ({self.position}, {self.duration} km)"
