from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class Tour(models.Model):
    EXPERINCE_CHOICES = (
        ("Excellent", "Excellent"),
        ("Very Good", "Very Good",),
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Bad", "Bad"),
    )
    TRAVEL_MODE_CHOICES = (
        ("Road", "Road"),
        ("Rail", "Rail"),
        ("Flight", "Flight"),
        ("Water Transport", "Water Transport")
    )

    TITLE_CHOICES = (
        ("Family Visit", "Family Visit"),
        ("Bussiness", "Bussineess"),
        ("Pilgrimage", "Pilgrimage"),
        ("Health Purpose", "Health Purpose"),
        ("Adventure", "Adventure"),
        ("Academics", "Academics")
    )


    title = models.CharField(choices=TITLE_CHOICES, max_length=200)
    tour_Purpose = models.CharField(max_length=100)
    Destination = CountryField(blank_label="Select Destination")
    continent = models.CharField(max_length=100)
    tour_description = models.TextField(blank=True, null=True)
    tour_transport_mode = models.CharField(choices=TRAVEL_MODE_CHOICES, max_length=100)
    tour_start_date = models.DateField()
    tour_end_date = models.DateField()
    experience = models.CharField(choices=EXPERINCE_CHOICES, max_length=200)

    def __str__(self):
        return self.title
    



