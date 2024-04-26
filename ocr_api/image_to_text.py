from django.conf import settings
from PIL import Image
import pytesseract

# location where pytesseract is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract'

def image_to_text(image_path):
    complete_image_path = f'{settings.BASE_DIR}/media/{image_path}' # create the path for the image
    with Image.open(complete_image_path, 'r') as image: # open the image using pillow
        text_from_image = pytesseract.image_to_string(image) # converts text in image to actual string
        return text_from_image