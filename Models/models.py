from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
from markdownx.models import MarkdownxField

# Create your models here.





class Account(AbstractUser):
    OrgRole = [(1, 'President'),(2, 'Internal Vice President'), (3, 'External Vice President'),
    (4, 'Treasurer'), (5, 'Secretary'), 
    (6, "Assistant Secretary"), (7, "Auditor"), (8, "Outreach Program Director"), (9, "Event Coordinator"),
    (10, "Public Information Officer"), (11, "Digital Officer"), (12, "Representative"), (13, 'Member')
    
    
    ]
    role = models.IntegerField(choices=OrgRole, null = True, blank=True)
    image_link = models.CharField(max_length=555, default = "https://preview.redd.it/h5gnz1ji36o61.png?width=225&format=png&auto=webp&s=84379f8d3bbe593a2e863c438cd03e84c8a474fa")
    description = models.CharField(max_length=255, default="Description")
    facebook_link = models.CharField(max_length=555, default = "https://www.facebook.com")
    

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password=password, is_staff=True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return
    class Meta:
        ordering = ['role']
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Announcements(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = MarkdownxField(max_length=10000)
    date = models.DateTimeField(default = timezone.now)
    thumbnail = models.ImageField(null = True, blank=True)

    def __str__(self):
        return f"{self.title} | {self.author}"
    



class Messages(models.Model):
    email = models.CharField(max_length=64)
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    msg = models.CharField(max_length=1028)