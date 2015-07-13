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
    ksagid = models.CharField('KSAG ID', primary_key=True, max_length=10)

    # Name of KSAG group
    name = models.CharField('KSAG name', max_length=300)

    # Category ID number
    categoryid = models.CharField('Ebisu category ID', max_length=10)
    
    # Name of category group
    categoryname = models.CharField('Ebisu category name', max_length=300)
    
    # Brand ID number
    brandid  = models.CharField('Brand ID', max_length=10)
   
    # Brand name
    brandname = models.CharField('Brand name', max_length=300)

    # String representation
    def __str__(self):

        return "KSAG " + self.ksagid

class Sku(models.Model):

# SKU object model.

    # Each Sku belongs to a Ksag (a Many-to-One relationship)
    ksag_num = models.ForeignKey(Ksag)

    # SKU ID number is primary key
    matchsku = models.CharField("Blick SKU ID", primary_key=True, max_length=20)
    
    # Item descrption
    descr = models.CharField("Item description", max_length=300)

    # String representation
    def __str__(self):
        
        return "Blick SKU " + self.matchsku

class CompSku(models.Model):

# Competitor SKU object model

    # Each CompSku belongs to a Sku (a Many-to-One relationship)
    parent_sku = models.ForeignKey(Sku)

    # Competitor SKU number is primary key
    sku = models.CharField('SKU ID', primary_key=True,
                               max_length=50)

    # Competitor name
    sellername = models.CharField('Seller name', max_length=300)

    # Competitor ID number
    sellerid = models.CharField('Seller ID', max_length=10)

    # Item description (may differ from parent Sku)
    descr = models.CharField('Item description', max_length=300)

    # List price
    listprice = models.CharField('List price', max_length=10)

    # Current price - what they are selling it for right now
    curprice = models.CharField('Current price', max_length=10)

    # Date on which this information was collected/crawled (NOT when
    # the JSON export was pulled from Ebisu
    date = models.CharField('Date crawled', max_length=10)

    # String representation
    def __str__(self):

        return self.competitor_name + ": " + self.sku 
        
class Map(models.Model):

# MAP info object model

    # Each MAP belongs to a Sku (though not all Skus have a MAP)
    parent_sku = models.ForeignKey(Sku)

    # SKU ID number is primary key
    sku = models.CharField('SKU ID', primary_key=True, max_length=20)

    # Percent at which item is usually discounted
    basepercent = models.CharField('Base percent discount', max_length=5)

    # Percent at which item is now being discounted
    percent = models.CharField('Current percent discount', max_length=5)

    # Ebisu editor link
    editorlink = models.CharField('Ebisu editor link', max_length=200)

    # String representation
    def __str__(self):

        return "MAP info for SKU " + self.sku

class Promotion(models.Model):

# Promotion info for a SKU

    # Each Promotion belongs to a Sku (not all Skus have a promotion)
    parent_sku = models.ForeignKey(Sku)
    
    # Start date of promo
    startdate = models.CharField('Start date', max_length=10)

    # End date of promo
    enddate = models.CharField('End date', max_length=10)

    # Promotion name/title
    name = models.CharField('Promotion name', max_length=300)

    # Percent discount of promotion
    percent = models.DecimalField('Promotion discount', max_length=5),

    # String representation
    def __str__(self):

        return "Promo for SKU " + str(self.parent_sku)



























