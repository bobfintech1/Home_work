from django.db import models


class VacancyModel(models.Model):
    title1 = models.CharField(max_length=255)
    body1 = models.TextField()
    title2 = models.CharField(max_length=255)
    body2 = models.TextField()
    pochta = models.EmailField()

    def __str__(self):
        return str(self.title1)