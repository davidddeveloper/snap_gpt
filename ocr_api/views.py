from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ImageText
from .serializers import ImageTextSerializer
from .image_to_text import image_to_text
from gpt4all import GPT4All
import json

# Createapi_view your views here.
@api_view(["GET"])
def image_text(request):
    image_texts = ImageText.objects.all()
    serializer = ImageTextSerializer(image_texts, many=True)
    
    return Response(serializer.data)

@api_view(["GET"])
def retrive_image_text(request, pk):
    image_text = ImageText.objects.get(id=pk)
    serializer = ImageTextSerializer(image_text)

    return Response(serializer.data)

@api_view(["POST"])
def create_image_text(request):
    """creates an image text using serializers"""

    serializer = ImageTextSerializer(data=request.data) # converts data to the respective object
    if serializer.is_valid(): # checks if the data is valid
        serializer.save() # saves the object to the database
        return HttpResponseRedirect(reverse('convert_to_text', kwargs={'pk': serializer.data['id']}))
    
    return redirect('frontend:home')

def convert_to_text(request, pk):
    imagetext = ImageText.objects.get(id=pk)

    text_from_image = image_to_text(imagetext.image) # call ocr function
    if text_from_image == '': # no text was extract from image
        return redirect('frontend:home')
    imagetext.text_from_image = text_from_image # save output of ocr to the object attribute
    imagetext.save() # reflect the latest changes to the object

    url = reverse('frontend:snapgpt') + f'?data={imagetext.text_from_image}'
    return redirect(url) 
    #return HttpResponseRedirect(reverse('frontend:snapgpt', args=[imagetext.text_from_image]))



#def retrive_text(request):http://127.0.0.1:8000/api_v1/chatbot
 #   return HttpResponse("Api for retriving the text from the image")