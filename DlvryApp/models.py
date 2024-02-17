from django.db import models
from enum import Enum

# Create your models here.
class ItemType(Enum):
    perishable = "PERISHABLE"
    non_perishable = "NON-PERISHABLE"
    
class Organization(models.Model):
    org_id = models.CharField(max_length = 100)
    org_name = models.CharField(max_length = 100)
    
class Item(models.Model):
    item_id = models.CharField(max_length = 100)
    item_name = models.CharField(max_length = 100, default='Item_Picture')
    item_pic = models.ImageField(upload_to='Item_Image', null=True, blank=True)
    item_type = models.CharField(max_length = 100 , choices = [(item_type.value,item_type.name) for item_type in ItemType ])
    description = models.TextField()
     
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item_id'], name='unique_item_id_no')
        ]
    
class Pricing(models.Model):
    organization =  models.ForeignKey(Organization,default = None,  on_delete = models.CASCADE, related_name='orgnize_id')
    item=  models.ForeignKey(Item,default = None,  on_delete = models.CASCADE, related_name='items_id')
    zone = models.CharField(max_length = 100)
    base_distance_in_km =  models.IntegerField(null = True)
    km_price = models.FloatField()
    fix_price = models.IntegerField(null = True)