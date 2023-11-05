from django.db import models

# Create your models here.

class TTS(models.Model):
    audio_file = models.FileField(upload_to = 'static/audio')