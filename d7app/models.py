from django.db import models

# Create your models here.
class samsung_phone(models.Model):
    Mobile_Companny= models.CharField(max_length=200, null= True)
    Mobile_Name= models.CharField(max_length=300, null= True)
    Whats_new= models.TextField( null= True)
    Chip=models.CharField(max_length=500, null= True)  
    Colors=models.CharField(max_length=300, null= True) 
    Cpu=models.CharField(max_length=500, null= True)
    Dimensions=models.CharField(max_length=300, null= True)
    Gpu=models.CharField(max_length=500, null= True)
    Resolution=models.CharField(max_length=500, null= True)
    Size=models.FloatField(null=True)
    Weight=models.IntegerField(null= True)
    price=models.IntegerField( null= True)
    rating=models.FloatField(null= True)
    OS=models.CharField(max_length=300, null= True)
    imagepath1=models.CharField(max_length=300,null=True)
    imagepath2=models.CharField(max_length=300,null=True)
    battery=models.CharField(max_length=400,null=True)
    back_camera=models.CharField(max_length=400,null=True)
    def __str__(self):
        return self.Mobile_Name
    class Meta:
        verbose_name_plural="samsungphone"