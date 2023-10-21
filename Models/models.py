from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
# Create your models here.





class Account(AbstractUser):
    OrgRole = [(1, 'President'),(2, 'Internal Vice President'), (3, 'External Vice President'),
    (4, 'Treasurer'), (5, 'Secretary'), 
    (6, "Assistant Secretary"), (7, "Auditor"), (8, "Outreach Program Director"), (9, "Event Coordinator"),
    (10, "Public Information Officer"), (11, "Digital Officer"), (12, "Representative"), (13, 'Member')
    
    
    ]
    role = models.IntegerField(choices=OrgRole)
    image_link = models.CharField(max_length=555, default = "https://preview.redd.it/h5gnz1ji36o61.png?width=225&format=png&auto=webp&s=84379f8d3bbe593a2e863c438cd03e84c8a474fa")
    description = models.CharField(max_length=255, default="Description")
    facebook_link = models.CharField(max_length=555, default = "https://www.facebook.com")

    REQUIRED_FIELDS = ["role"]

    class Meta:
        ordering = ['role']
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Announcements(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.title} | {self.author}"



