from django.db import models


# Create your models here.
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)


class Logger(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length=200)
    # shift = models.ChoiceField(choices = SHIFT) to be refactored
    time_log = models.TimeField(help_text="Enter exact time")

    def __str__(self):
        return self.first_name

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length =200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now = True)
    comments = models.CharField(max_length = 1000)

    def __str__(self):
        return self.first_name