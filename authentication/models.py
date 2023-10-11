from django.db import models
from django.utils import timezone

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class membersModel(baseModel):
    first_name = models.CharField(max_length=255, null=False, blank= False)
    last_name = models.CharField(max_length=255, null=False, blank= False)
    email = models.EmailField(max_length=255, null=False, blank= False, unique= True)
    mobile = models.CharField(max_length=20, null=False, blank= False, unique= True)
    password = models.CharField(max_length=255, null=False, blank= False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        # Convert email and mobile to lowercase before saving
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        self.email = self.email.lower()
        self.mobile = self.mobile.lower()
        super(membersModel, self).save(*args, **kwargs)
    

class memberProfileModel(baseModel):
    GENDER_OPTIONS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    member_id = models.ForeignKey(membersModel, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="member_profiles/")
    gender = models.CharField(max_length=20, choices=GENDER_OPTIONS)