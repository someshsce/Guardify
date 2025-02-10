'''from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from django.core.mail import EmailMessage
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        instance = serializer.save()

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
        }}
        .container {{
            width: 90%;
            margin: auto;
            background-color: #ffffff;
            padding: 5px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #444444;
            border-bottom: 1px solid #dddddd;
            padding-bottom: 10px;
        }}
        p {{
            color: #666666;
        }}
        </style>
        </head>
        <body>
        <div class="container">
            <h1>Contact Request from {instance.name}</h1>
            <p><strong>Name:</strong> {instance.name}</p>
            <p><strong>Email:</strong> {instance.email}</p>
            <p><strong>Subject:</strong> {instance.subject}</p>
            <p><strong>Message:</strong> {instance.message}</p>
        </div>
        </body>
        </html>
        """

        email = EmailMessage(
            f'Contact Request #{instance.id} from {instance.name}',
            html_content,
            'Team Guardify <hackify1@gmail.com>',
            ['pradoshpandav123@gmail.com'],
        )
        email.content_subtype = 'html'
        email.send(fail_silently=False)

        instance.delete()

        return Response({'detail': 'Form submitted successfully!'}, status=status.HTTP_201_CREATED)
'''

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Contact

@method_decorator(csrf_exempt, name='dispatch')
class ContactCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        if not all([name, email, subject, message]):
            return JsonResponse({'error': 'All fields are required!'}, status=400)
        
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
        }}
        .container {{
            width: 90%;
            margin: auto;
            background-color: #ffffff;
            padding: 5px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #444444;
            border-bottom: 1px solid #dddddd;
            padding-bottom: 10px;
        }}
        p {{
            color: #666666;
        }}
        </style>
        </head>
        <body>
        <div class="container">
            <h1>Contact Request from {contact.name}</h1>
            <p><strong>Name:</strong> {contact.name}</p>
            <p><strong>Email:</strong> {contact.email}</p>
            <p><strong>Subject:</strong> {contact.subject}</p>
            <p><strong>Message:</strong> {contact.message}</p>
        </div>
        </body>
        </html>
        """

        email = EmailMessage(
            f'Contact Request #{contact.id} from {contact.name}',
            html_content,
            'Team Guardify <hackify1@gmail.com>',
            ['someshs.ce@gmail.com'],
        )

        email.content_subtype = 'html'

        email.send(fail_silently=False)

        contact.delete()

        return JsonResponse({'detail': 'Form submitted successfully!'}, status=201)
