from django.forms import ModelForm
from Models.models import Announcements
from API.models import TTS
class TTSForm(ModelForm):
    class Meta:
        model = TTS
        fields = ['audio_file']