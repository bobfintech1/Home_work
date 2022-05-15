from django.db import models
from core.models.home import upload_location


class ServicesModel(models.Model):
    img_1 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_2 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_3 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_4 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_5 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_6 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    title_1 = models.TextField()
    title_2 = models.TextField()
    title_3 = models.TextField()
    title_4 = models.TextField()
    title_5 = models.TextField()
    title_6 = models.TextField()

    @property
    def imageURL(self):
        try:
            url = str(self.img.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title_1)
