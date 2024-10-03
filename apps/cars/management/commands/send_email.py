from django.core.management.base import BaseCommand

from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send email'
    
    def handle(self, *args, **kwargs):
        send_mail('Test mail', 'This is test mail', 'utubahmad031@gmail.com', 
                  ['utubahmad031@gmail.com'], fail_silently=False)
        self.stdout.write(self.style.SUCCESS('Email sent!'))
        