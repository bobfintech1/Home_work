from django.db import models
from core.models.home import upload_location


class ServicesModel(models.Model):
    img_1 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_2 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_3 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_4 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_5 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_6 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    title = models.TextField()
    title_1 = models.TextField()
    title_2 = models.TextField()
    title_3 = models.TextField()
    title_4 = models.TextField()
    title_5 = models.TextField()
    title_6 = models.TextField()

    @property
    def image1URL(self):
        try:
            url = str(self.img_1.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title)

    @property
    def image2URL(self):
        try:
            url = str(self.img_2.url)
        except:
            url = ''

        return url    \

    @property
    def image3URL(self):
        try:
            url = str(self.img_3.url)
        except:
            url = ''

        return url

    @property
    def image4URL(self):
        try:
            url = str(self.img_4.url)
        except:
            url = ''

        return url

    @property
    def image5URL(self):
        try:
            url = str(self.img_5.url)
        except:
            url = ''

        return url


    @property
    def image6URL(self):
        try:
            url = str(self.img_6.url)
        except:
            url = ''

        return url