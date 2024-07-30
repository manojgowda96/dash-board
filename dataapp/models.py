from django.db import models

# Create your models here.

class Data(models.Model):
    end_year = models.CharField(max_length=10, blank=True, null=True)
    intensity = models.IntegerField(default=0)
    sector = models.CharField(max_length=100,blank=True, default="")
    topic = models.CharField(max_length=250,blank=True, default="")
    insight = models.TextField(blank=True,default="")
    url = models.URLField(max_length=200,blank=True,default="")
    region = models.CharField(max_length=100, null='True',blank=True)
    start_year = models.IntegerField( blank=True, null=True)
    impact = models.CharField(max_length=100, blank=True, default='')
    added = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, default='')
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=100, null=True)
    title = models.TextField(max_length=300,null=True)
    likelihood = models.IntegerField(null=True,default="")
    # relevance = models.IntegerField()
    # year = models.IntegerField()
    # country = models.CharField(max_length=100)
    # topics = models.CharField(max_length=250)
    # region = models.CharField(max_length=100)
    # city = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.topic} - {self.country}"