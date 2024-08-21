from django.shortcuts import render, HttpResponse, redirect
from Models.models import * 
from UserInterface.forms import TTSForm
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
import openai
import json
import environ
env = environ.Env()
openai.api_key = env('API_KEY')


# Credits to stackoverflow for this 404 catcher 
def bad_request(request, exception):
    return redirect('index')

# Credits to stackoverflow for this genius hack 
def get_referer(request):
    is_HTMX = request.META.get('HTTP_HX_REQUEST')
    if not is_HTMX:
        return False 
    
    else:
        return True
def index(request):
    """
    Renders the index page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered index page.
    """
    if get_referer(request):
        return render(request, 'UserInterface/partition/index.html')
    else:
        return render(request, 'UserInterface/index.html')



def coding_ai(request):
    
    if get_referer(request):
        return render(request, 'UserInterface/partition/coding_ai.html')
    else:
        return render(request, 'UserInterface/coding_ai.html')


def html_prettier(request):
    if get_referer(request):
        return render(request, 'UserInterface/partition/html_prettier.html')
    else:
        return render(request, 'UserInterface/html_prettier.html')
    
def upload_file(request):
    if request.method == "GET":
        items = {
            'form': TTSForm(),
        }
        if get_referer(request):
            return render(request, 'UserInterface/partition/TTS.html', context = items)
        else:
            return render(request, 'UserInterface/TTS.html', context = items)
    elif request.method == "POST":
        form =TTSForm(request.POST, request.FILES)
        if form.is_valid:
           

            transcript = openai.Audio.translate(model="whisper-1", file = request.FILES['audio_file'], response_format="text")
            transcript = transcript.replace("Transcriber's Name Reviewer's Name Timing & Transcription by Rev.com", "")
            return HttpResponse(json.dumps(transcript))