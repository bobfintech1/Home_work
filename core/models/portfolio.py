from django.db import models
from core.models.home import upload_location


class PortfolioModel(models.Model):
    title = models.CharField(max_length=255)
    commit = models.TextField()
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)
    imge = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_2 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_3 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_4 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    img_5 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    body = models.TextField()
    body_1 = models.TextField()
    body_2 = models.TextField()
    body_3 = models.TextField()
    body_4 = models.TextField()
    body_5 = models.TextField()

    @property
    def imageURL(self):
        try:
            url = str(self.img.url)
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.title)


    @property
    def image1URL(self):
        try:
            url = str(self.imge.url)
        except:
            url = ''

        return url


    @property
    def image2URL(self):
        try:
            url = str(self.img_2.url)
        except:
            url = ''

        return url

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
