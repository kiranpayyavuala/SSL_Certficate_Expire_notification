from django.db import models
import datetime

class SSLCertificate(models.Model):
    domain_name = models.CharField(max_length=255)
    created_date = models.DateField()
    expire_date = models.DateField()
    sop_link = models.URLField()
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    product_details = models.TextField(blank=True)

    def days_until_expire(self):
        if self.expire_date:
            return (self.expire_date - datetime.date.today()).days
        return None
