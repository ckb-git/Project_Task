from django.db import models

import random

import string




# Create your models here.
def key_generator():
    key =''.join(random.choice(string.digits) for x in range(6))
    if Inventory.objects.filter(iin=key).exists():
        key = key_generator()
    return key

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True)
    iin = models.CharField(max_length=6, default=key_generator, unique=True, editable=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    quantity_sold = models.PositiveIntegerField(null=True,blank=True,default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    profit_earned = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)


    class Meta:  
        db_table = "inventory"

   


class Orders(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    # t_cost = models.DecimalField(max_digits=10, decimal_places=2,blank=True)

    # @property
    # def t_cost(self):  
    #     return self.quantity * self.item.selling_price 
    


    class Meta:  
        db_table = "orders"

class Transaction(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True)
    orid = models.ForeignKey(Orders, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True)
    # transactiondttm = models.DateTimeField()

    class Meta:  
        db_table = "transaction"

