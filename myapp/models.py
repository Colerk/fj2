from django.db import models
#from location_field.models.plain import PlainLocationField

# Create your models here.
class JournalRecord(models.Model):
        species_choice = (
        ('Chum', 'Chum'),
        ('Coho', 'Coho'),
        ('Chinook', 'Chinook'),
        ('Pink', 'Pink'),
        ('Sockeye', 'Sockeye'),
        ('Trout', 'Trout')
        )
        size = models.FloatField()
        species = models.CharField(max_length=50, choices=species_choice)
        location = models.CharField(max_length=100)
        latitude = models.FloatField()
        longitude = models.FloatField()
        #location = PlainLocationField(based_fields=['city'], zoom=7)
        date = models.CharField(max_length=100)
        method = models.CharField(max_length=300)

        def __str__(self):
            return str(self.size) + " lbs" + " " + self.species +  " - " + self.location + " - " + self.date + " - " + self.method
