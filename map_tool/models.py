# models.py
#
# Elizabeth Bentivegna
# Data models for the KSAG, SKU, and CompSKU objects.
#
# TODO: MAP models

from django.db import models


class Ksag(models.Model):

# KSAG object model.
   
    # KSAG number is primary key 
    ksag_num = models.IntegerField(primary_key=True)

    # Name of KSAG group
    name = models.CharField(max_length=300)

    # Category ID number
    category_num = models.IntegerField('Ebisu category ID')
    
    # Name of category group
    category_name = models.CharField(max_length=300)
    
    # Brand ID number
    brand_num  = models.IntegerField()
   
    # Brand name
    brand_name = models.CharField(max_length=300)


class Sku(models.Model):

# SKU object model.

    # Each Sku belongs to a Ksag (a Many-to-One relationship)
    ksag_num = models.ForeignKey(Ksag)

    # SKU ID number is primary key
    sku_num = models.CharField(primary_key=True, max_length=20)
    
    # Item descrption
    description = models.CharField(max_length=300)


class CompSku(models.Model):

# Competitor SKU object model

    # Each CompSku belongs to a Sku (a Many-to-One relationship)
    parent_sku = models.ForeignKey(Sku)

    # Competitor SKU number is primary key
    sku_num = models.CharField(primary_key=True,
                               max_length=50)

    # Competitor name
    competitor_name = models.CharField(max_length=300)

    # Competitor ID number
    competitor_num = models.IntegerField()

    # Item description (may differ from parent Sku)
    description = models.CharField(max_length=300)

    # List price
    list_price = models.DecimalField(max_digits=10, 
                                    decimal_places=2)

    # Current price - what they are selling it for right now
    current_price = models.DecimalField(max_digits=10, 
                                       decimal_places=2)


    # Date on which this information was collected/crawled (NOT when
    # the JSON export was pulled from Ebisu
    date_crawled = models.DateTimeField()

class Map(models.Model):

# MAP info object model

    # Each MAP belongs to a Sku (though not all Skus have a MAP)
    parent_sku = models.ForeignKey(Sku)

    # SKU ID number is primary key
    sku_num = models.CharField(primary_key=True, max_length=20)

    # Percent at which item is usually discounted
    base_percent = models.DecimalField(max_digits=4,
                               decimal_places=2)

    # Percent at which item is now being discounted
    current_percent = models.DecimalField(max_digits=4,
                                  decimal_places=2)

class Promotion(models.Model):

# Promotion info for a SKU

    # Each Promotion belongs to a Sku (not all Skus have a promotion)
    parent_sku = models.ForeignKey(Sku)
    
    # Start date of promo
    start_date = models.DateTimeField()

    # End date of promo
    end_date = models.DateTimeField()

    # Promotion name/title
    name = models.CharField(max_length=300)

    # Percent discount of promotion
    percent = models.DecimalField(max_digits=4,
                                  decimal_places=2)





























