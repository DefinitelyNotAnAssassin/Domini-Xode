from django.forms import ModelForm
from Models.models import Announcements


class ArticleForm(ModelForm):
    class Meta:
        model = Announcements
        fields = ["content"]
