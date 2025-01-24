from django import forms
from .models import SSLCertificate

class SSLCertificateForm(forms.ModelForm):
    class Meta:
        model = SSLCertificate
        fields = ['domain_name', 'created_date', 'expire_date', 'sop_link', 'status', 'product_details']
        widgets = {
            'created_date': forms.DateInput(attrs={'type': 'date'}),
            'expire_date': forms.DateInput(attrs={'type': 'date'}),
        }
