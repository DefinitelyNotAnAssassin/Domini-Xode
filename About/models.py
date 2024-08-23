from django.db import models
import os
# Create your models here.


class Year(models.Model):
    """
    Represents a school year.
    """
    year = models.CharField(max_length=9, unique=True)
    image = models.ImageField(upload_to='year_images/', blank=True, null=True) 
    def __str__(self):
        return self.year 
    
    
    
def upload_to_officer_images(instance, filename):
    return os.path.join('officer_images', str(instance.year), filename)

class Officer(models.Model): 
    """
    Represents an officer in the organization.
    """
    OrgRole = [(1, 'President'),(2, 'Internal Vice President'), (3, 'External Vice President'),
               (4, 'Treasurer'), (5, 'Secretary'),
               (6, "Assistant Secretary"), (7, "Auditor"), (8, "Outreach Program Director"), (9, "Event Coordinator"),
               (10, "Public Information Officer"), (11, "Digital Officer"), (12, "Representative"), (13, "Technical"), (14, "Documentation"), (15, 'Member')
              ]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=OrgRole)
    image = models.ImageField(upload_to=upload_to_officer_images, blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

