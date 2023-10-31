from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
from markdownx.models import MarkdownxField

class Account(AbstractUser):
    """
    Custom user model representing an account in your organization.

    Attributes:
        role (int): The role of the user in the organization.
        image_link (str): Link to the user's profile image.
        description (str): A short description about the user.
        facebook_link (str): Link to the user's Facebook profile.

    Methods:
        save(): Overrides the save method to set the user's password securely.
        create_superuser(): Creates a superuser with specific attributes.

    Meta:
        ordering: Order users by their 'role' attribute.

    __str__(): Returns a string representation of the user.

    Inherits from AbstractUser.
    """
    OrgRole = [(1, 'President'),(2, 'Internal Vice President'), (3, 'External Vice President'),
               (4, 'Treasurer'), (5, 'Secretary'), 
               (6, "Assistant Secretary"), (7, "Auditor"), (8, "Outreach Program Director"), (9, "Event Coordinator"),
               (10, "Public Information Officer"), (11, "Digital Officer"), (12, "Representative"), (13, 'Member')
              ]
    role = models.IntegerField(choices=OrgRole, null=True, blank=True)
    image_link = models.CharField(max_length=555, default="https://preview.redd.it/h5gnz1ji36o61.png?width=225&format=png&auto=webp&s=84379f8d3bbe593a2e863c438cd03e84c8a474fa")
    description = models.CharField(max_length=255, default="Description")
    facebook_link = models.CharField(max_length=555, default="https://www.facebook.com")

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the user's password securely.

        Args:
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        """
        if not self.pk: 
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates a superuser with specific attributes.

        Args:
            username (str): The username for the superuser.
            email (str): The email address for the superuser.
            password (str): The password for the superuser.
            **extra_fields: Additional fields for the superuser.
        """
        user = self.create_user(username, email, password=password, is_staff=True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return

    class Meta:
        ordering = ['role']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Announcements(models.Model):
    """
    Model representing announcements or articles.

    Attributes:
        title (str): The title of the announcement or article.
        author (Account): The author of the announcement, linked to the Account model.
        content (MarkdownxField): The content of the announcement in Markdown format.
        date (datetime): The date when the announcement was created.
        thumbnail (ImageField): An optional thumbnail image for the announcement.

    Methods:
        __str__(): Returns a string representation of the announcement.
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = MarkdownxField(max_length=10000)
    date = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(null=True, blank=True, default  = 'static/img/domini_xode_logo.jpg', upload_to='static/img/')

    def __str__(self):
        return f"{self.title} | {self.author}"


class Messages(models.Model):
    """
    Model representing contact messages.

    Attributes:
        email (str): The email address of the sender.
        full_name (str): The sender's full name.
        phone_number (str): The sender's phone number.
        msg (str): The message content.

    Methods:
        None
    """
    email = models.CharField(max_length=64)
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    msg = models.CharField(max_length=1028)


class Events(models.Model):
    event_name = models.CharField(max_length=64)
    event_description = models.CharField(max_length=1028)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_location = models.CharField(max_length=32)
    event_registration_link = models.CharField(max_length=256, blank = True, null = True)
    event_status = models.CharField(max_length=32, blank = True, null = True,default = 'Upcoming')
    event_flyer = models.FileField(blank = True, null = True, upload_to='Models/static')
    
    def __str__(this):
        return f'{this.event_name}'