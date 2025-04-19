# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Wallet(models.Model):

    #__Wallet_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    size = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    #__Wallet_FIELDS__END

    class Meta:
        verbose_name        = _("Wallet")
        verbose_name_plural = _("Wallet")


class Position(models.Model):

    #__Position_FIELDS__
    symbol = models.TextField(max_length=255, null=True, blank=True)
    instrument = models.TextField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    change_percent = models.TextField(max_length=255, null=True, blank=True)
    buy_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sell_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    buy_price = models.TextField(max_length=255, null=True, blank=True)
    sell_price = models.TextField(max_length=255, null=True, blank=True)
    buy_fee = models.TextField(max_length=255, null=True, blank=True)
    sell_fee = models.TextField(max_length=255, null=True, blank=True)
    other_fees = models.TextField(max_length=255, null=True, blank=True)
    buy_vol = models.TextField(max_length=255, null=True, blank=True)
    sell_vol = models.TextField(max_length=255, null=True, blank=True)
    buy_value = models.TextField(max_length=255, null=True, blank=True)
    sell_value = models.TextField(max_length=255, null=True, blank=True)
    remarks = models.TextField(max_length=255, null=True, blank=True)
    wallet = models.ForeignKey(wallet, on_delete=models.CASCADE)

    #__Position_FIELDS__END

    class Meta:
        verbose_name        = _("Position")
        verbose_name_plural = _("Position")


class Trade(models.Model):

    #__Trade_FIELDS__
    number = models.IntegerField(null=True, blank=True)
    wallet = models.ForeignKey(wallet, on_delete=models.CASCADE)
    symbol = models.TextField(max_length=255, null=True, blank=True)
    instrument = models.TextField(max_length=255, null=True, blank=True)
    market = models.TextField(max_length=255, null=True, blank=True)
    buy_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    buy_vol = models.TextField(max_length=255, null=True, blank=True)
    buy_price = models.TextField(max_length=255, null=True, blank=True)
    buy_fee = models.TextField(max_length=255, null=True, blank=True)
    buy_value = models.TextField(max_length=255, null=True, blank=True)
    sell_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sell_vol = models.TextField(max_length=255, null=True, blank=True)
    sell_price = models.TextField(max_length=255, null=True, blank=True)
    sell_fee = models.TextField(max_length=255, null=True, blank=True)
    sell_value = models.TextField(max_length=255, null=True, blank=True)
    other_fees = models.TextField(max_length=255, null=True, blank=True)

    #__Trade_FIELDS__END

    class Meta:
        verbose_name        = _("Trade")
        verbose_name_plural = _("Trade")



#__MODELS__END
