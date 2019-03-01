from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this company.
        """
        return reverse('Companies_Detail', args=[str(self.id)])

class Envelope(models.Model):
    amount = models.IntegerField()
    motive = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name+" - "+self.motive
