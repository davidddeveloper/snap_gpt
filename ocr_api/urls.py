from django.urls import path
from . import views


# api routes
# get_all the imagetext
urlpatterns = [
    path('image_text', views.image_text, name='image_text'),
    path('retrive_image_text', views.retrive_image_text, name='retrive_image_text'),
    path('create_image_text', views.create_image_text, name='create_image_text'),
    path('convert_to_text/<str:pk>', views.convert_to_text, name='convert_to_text')
]