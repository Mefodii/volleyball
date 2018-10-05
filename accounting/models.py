from django.db import models


# Create your models here.
class Payment(models.Model):
    event_id = models.ForeignKey("event.Event",
                                 verbose_name="Event",
                                 on_delete=models.CASCADE)
    voleibalist_id = models.ForeignKey("event.Voleibalist",
                                       verbose_name="Voleibalist",
                                       on_delete=models.CASCADE)
    amount = models.IntegerField()


class Expense(models.Model):
    description = models.CharField(max_length=300,
                                   verbose_name="Expense description",
                                   help_text="For what purposes was the expense")
    amount = models.IntegerField()
    date = models.DateTimeField()
