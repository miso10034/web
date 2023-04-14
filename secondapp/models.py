from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField

class Cart(models.Model):
    cart_member = CharField(max_length=15, null=False)
    cart_no = CharField(primary_key = True, max_length=13, null=False)
    cart_prod = CharField(max_length=10, null=False)
    cart_qty = IntegerField(max_length=8, null=False)

    class Meta:
        db_table = "cart"
        app_label="secondapp"
        managed = False