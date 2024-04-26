from django.shortcuts import render
from django.http.response import JsonResponse
import json
from gpt4all import GPT4All
import google.generativeai as genai

genai.configure(api_key='AIzaSyDBKIaezc9aYwo3Zr6GUCG0N5MC25Azlmw')

# Create your views here.
#def chatbot_view(request):
    #if request.method == 'POST':
        #data = json.loads(request.body.decode('utf-8'))
        #user_input = data.get('user_prompt') # get user input
        #with GPT4All("orca-mini-3b-gguf2-q4_0.gguf").chat_session() as model:
            #response = model.generate(prompt=user_input, temp=0)
            #return JsonResponse({'response': response})
        

#gemini ai
def chatbot_view(request):
    model = genai.GenerativeModel('gemini-pro')

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_input = data.get('user_prompt') # get user input
        
        # generate response
        print(user_input)
        response = model.generate_content(user_input)
        print(response)

        return JsonResponse({'response': response.text})
