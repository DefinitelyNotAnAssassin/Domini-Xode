from django.shortcuts import render, HttpResponse
import json
from django.http import StreamingHttpResponse
import openai
from markdownx.utils import markdownify
import environ
env = environ.Env()
openai.api_key = env('API_KEY')



def codeit(request):
    arg = request.GET.get('msg', '')
    print(arg)
    complete_message = []
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[
    {"role": "user", "content": f"Answer strictly in markdown syntax:{arg}"},],max_tokens = 1000, temperature = 0.2, stream = True)
    for chunk in completion:
        try:
            complete_message.append(chunk['choices'][0]['delta']['content'])
        except KeyError:
            pass

    
    complete_message = ''.join(complete_message)
    complete_message = markdownify(complete_message)
    
    return HttpResponse(json.dumps(complete_message))
