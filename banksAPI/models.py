from django.db import models

class Branch(models.Model):
    bank_id = models.IntegerField()
    branch_id = models.IntegerField()
    branch_name = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    bank_branch_id = models.IntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    phone = models.CharField(max_length=255)
