import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from certificates.models import SSLCertificate

class Command(BaseCommand):
    help = 'Send notifications for expiring SSL certificates'

    def handle(self, *args, **kwargs):
        today = timezone.now()
        upcoming_expirations = SSLCertificate.objects.filter(
            expire_date__lte=today + datetime.timedelta(days=15)
        )

        for cert in upcoming_expirations:
            days_left = cert.days_until_expire()
            if days_left <= 15:
                send_mail(
                    subject=f'SSL Certificate Expiration Warning: {cert.domain_name}',
                    message=f'The SSL certificate for {cert.domain_name} will expire in {days_left} days.\n\nSOP Link: {cert.sop_link}',
                    from_email='your_email@example.com',
                    recipient_list=['recipient@example.com'],
                )
                self.stdout.write(self.style.SUCCESS(f'Notification sent for {cert.domain_name}'))
