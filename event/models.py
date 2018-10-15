from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Voleibalist(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Voleibalist Name")
    alias = models.CharField(max_length=100,
                             verbose_name="Voleibalist Alias")
    user = models.ForeignKey(User,
                             verbose_name="Registered User",
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True)


class Event(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name="Event Name",
                            help_text="Write name of the Event")
    date = models.DateTimeField()
    duration = models.DecimalField(max_digits=2,
                                   decimal_places=1)
    price_per_hour = models.DecimalField(max_digits=5,
                                         decimal_places=1)
