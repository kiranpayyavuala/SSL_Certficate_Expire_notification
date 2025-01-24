from django.contrib import admin
from .models import SSLCertificate

class SSLCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain_name', 'created_date', 'expire_date', 'days_until_expire')
    list_filter = ('expire_date',)
    search_fields = ('domain_name', 'sop_link')

    def days_until_expire(self, obj):
        return obj.days_until_expire()
    days_until_expire.short_description = 'Days Until Expire'

admin.site.register(SSLCertificate, SSLCertificateAdmin)
