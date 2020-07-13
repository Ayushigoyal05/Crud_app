from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=100,null=False)
    role=models.CharField(max_length=150,null=False)
    phone=models.IntegerField()
    address=models.CharField(max_length=250,null=False)
    salary=models.IntegerField()


    def __str__(self):
        return str(self.name)+" "+str(self.role)
