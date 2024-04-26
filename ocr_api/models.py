from django.db import models

# Create your models here.
class ImageText(models.Model):
    image = models.ImageField(upload_to='images', null=True)
    text_from_image = models.TextField(null=True)

    def __str__(self):
        return "{}".format(self.id)