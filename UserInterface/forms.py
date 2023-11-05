from django.forms import ModelForm
from Models.models import Announcements
from API.models import TTS
class ArticleForm(ModelForm):
    class Meta:
        model = Announcements
        fields = ['content']

class TTSForm(ModelForm):
    class Meta:
        model = TTS
        fields = ['audio_file']