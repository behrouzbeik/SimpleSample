from django.db import models

# Create your models here.

class Pack(models.Model):
  trackingNumber = models.CharField(max_length=10)
  carrier = models.CharField(max_length=5)
  senderStreet = models.CharField(max_length=10)
  senderRegionalCode = models.CharField(max_length=10)
  senderCity = models.CharField(max_length=255)
  senderCountry = models.CharField(max_length=255)
  receiverStreet = models.CharField(max_length=10)
  receiverRegionalCode = models.CharField(max_length=10)
  receiverCity = models.CharField(max_length=255)
  receiverCountry = models.CharField(max_length=255)
  article = models.CharField(max_length=255)
  quantity = models.PositiveIntegerField()
  price = models.PositiveBigIntegerField()
  sku = models.CharField(max_length=10)
  status = models.CharField(max_length=20)