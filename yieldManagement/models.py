from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100, null=True)

class MarketPlaceModel(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    CheckIn0 = models.CharField(max_length=25, null=True)
    CheckIn1 = models.CharField(max_length=25, null=True)
    CheckIn2 = models.CharField(max_length=25, null=True)
    CheckIn3 = models.CharField(max_length=25, null=True)
    CheckIn4 = models.CharField(max_length=25, null=True)
    CheckIn5 = models.CharField(max_length=25, null=True)
    CheckIn6 = models.CharField(max_length=25, null=True)
    hotel = models.CharField(max_length=150, null=True)
    hotelId = models.CharField(max_length=25, null=True)
    review = models.CharField(max_length=25, null=True)
    location = models.CharField(max_length=200, null=True)
    locationId = models.CharField(max_length=500, null=True)

class WeekDays(models.Model):
    day0 = models.CharField(max_length=15, null=True)
    day1 = models.CharField(max_length=15, null=True)
    day2 = models.CharField(max_length=15, null=True)
    day3 = models.CharField(max_length=15, null=True)
    day4 = models.CharField(max_length=15, null=True)
    day5 = models.CharField(max_length=15, null=True)
    day6 = models.CharField(max_length=15, null=True)

class Strategies(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    years = models.CharField(max_length=50, null=True, default="All Years")
    months = models.CharField(max_length=50, null=True, default="All")
    weekdays = models.CharField(max_length=50, null=True, default="All")
    days = models.CharField(max_length=10, null=True, default="1")
    sold10 = models.CharField(max_length=25, null=True)
    sold15 = models.CharField(max_length=25, null=True)
    sold20 = models.CharField(max_length=25, null=True)
    sold40 = models.CharField(max_length=25, null=True)
    sold50 = models.CharField(max_length=25, null=True)
    sold60 = models.CharField(max_length=25, null=True)


class ThreShold(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    month = models.CharField(max_length=20, null=True)
    weekday = models.CharField(max_length=20, null=True)
    min_price = models.CharField(max_length=20, null=True)
    max_price = models.CharField(max_length=20, null=True)
    sellout = models.CharField(max_length=20, null=True)

class OverRide(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    fromDate = models.CharField(max_length=25, null=True)
    toDate = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=25, null=True)
    value = models.CharField(max_length=25, null=True)

class RoomTypeYield(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    roomType = models.CharField(max_length=25, default="NDD", null=True)
    min_price = models.CharField(max_length=25, null=True)
    max_price = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=25, null=True)
    single = models.CharField(max_length=25, null=True)
    double = models.CharField(max_length=25, null=True)
    triple = models.CharField(max_length=25, null=True)
    quad = models.CharField(max_length=25, null=True)

class NoteYield(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    fromDate = models.CharField(max_length=25, null=True)
    toDate = models.CharField(max_length=25, null=True)
    note = models.CharField(max_length=500, null=True)

class BudgetYield(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    monthlydate = models.CharField(max_length=25, null=True)
    capacity =  models.CharField(max_length=20, null=True)
    occInd = models.CharField(max_length=25, null=True)
    occGroup = models.CharField(max_length=25, null=True)
    occAllotment = models.CharField(max_length=25, null=True)
    occGroupTent = models.CharField(max_length=25, null=True)
    occAllotmentTent = models.CharField(max_length=25, null=True)

class ForecastYield(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    monthlydate = models.CharField(max_length=25, null=True)
    capacity =  models.CharField(max_length=20, null=True)
    occInd = models.CharField(max_length=25, null=True)
    occGroup = models.CharField(max_length=25, null=True)
    occAllotment = models.CharField(max_length=25, null=True)
    occGroupTent = models.CharField(max_length=25, null=True)
    occAllotmentTent = models.CharField(max_length=25, null=True)

class ReportYield(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    active = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=25, null=True)
    period = models.CharField(max_length=25, null=True)
    weekday = models.CharField(max_length=25, null=True)
    dayMonth = models.CharField(max_length=25, null=True)
    sendTo = models.CharField(max_length=25, null=True)

class CalenderYield(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    type = models.CharField(max_length=25, null=True)
    fromDate = models.CharField(max_length=20, null=True)
    toDate = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, null=True)














