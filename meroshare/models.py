from django.db import models

#MeroShare Model
class MeroShare(models.Model):  
    share_mnemonic = models.CharField(max_length=10,primary_key=True,unique=True)  
    share_name = models.CharField(max_length=200)  
    quantity = models.PositiveIntegerField(null=False,blank=False)
    purchase_price = models.FloatField(null=False,blank=False)    
    class Meta:  
        db_table = "meroshare"  
