from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=[('farmer', 'Farmer'), ('buyer', 'Buyer')], null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Crop(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

class Request(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_requests')
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    message = models.TextField(blank=True)

