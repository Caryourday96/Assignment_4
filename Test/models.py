from django.db import models

#ADETUNJI KAYODE
#Last Modified 23rd March
#This is where the database model and algorithm is created
# Create your models here.
from django.db import models

class Industry(models.Model):
    id = models.AutoField(primary_key=True)
    Ref_Date = models.CharField(max_length=100)
    GEO = models.CharField(max_length=100)
    COMMOD = models.CharField(max_length=100)
    Vector = models.CharField(max_length=100)
    Coordinate = models.CharField(max_length=100)
    Value = models.CharField(max_length=100)


#The field names must match the ones in the file to be uploaded. Case and spacing wise