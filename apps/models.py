from django.db import models

# Create your models here.
class company(models.Model):
    cname = models.CharField(max_length=100)
    company_id = models.IntegerField()


class department(models.Model):
    dname = models.CharField(max_length=100)
    dep_id = models.IntegerField(max_length=10)


class user(models.Model):
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=100,null=False)
    gender = models.CharField(max_length=100)
    company_id = models.ForeignKey(company,on_delete=models.CASCADE)
    dep_id = models.ForeignKey(department,on_delete=models.CASCADE)
