from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class RealEstate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="real_estate/", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    reserved = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile_url = models.URLField(null=True, blank=True)
    contact_phone = models.CharField(max_length=100, null=True, blank=True)
    total_sales = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class AgentRealEstate(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.agent.name} {self.real_estate.name}"


class Characteristic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CharacteristicRealEstate(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, null=True, blank=True)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.characteristic.name} {self.real_estate.name}"