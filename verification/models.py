from django.db import models

class Verification(models.Model):
    STATUS_CHOICES = [
        (0, 'Rejected'),
        (1, 'Verified'),
        (2, 'Pending'),
    ]

    type = models.CharField(max_length=50)
    doc_type = models.CharField(max_length=50)
    doc_image = models.ImageField(upload_to='documents/')
    audience = models.TextField(blank=True, null=True)
    known_as = models.BooleanField(default=False)
    personal_details = models.JSONField()
    doc_number = models.CharField(max_length=100)
    links = models.JSONField()
    address = models.JSONField()
    email = models.EmailField(unique=True) 
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)  
    def __str__(self):
        return self.personal_details.get("name", "Unknown")