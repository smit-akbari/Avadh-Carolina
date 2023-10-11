from django.db import models

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# suggestionModel 

class suggestionModel(baseModel):
    suggestion = models.TextField(max_length=255, null=False, blank= False)
    

    def __str__(self):
        return f"{self.id}"
    

class clubHouseBookingModel(baseModel):
    event_name = models.CharField(max_length=255, null=False, blank= False)
    from_date = models.DateField(max_length=30, null=False, blank=False)
    to_date = models.DateField(max_length=30, null=False, blank=False) 
    description = models.TextField(max_length=255, null=False, blank= False)

    def __str__(self):
        return f"{self.event_name}"