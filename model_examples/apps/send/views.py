from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):
    send_mail(
        "Hello from Vladimir Company",               # Asunto del email
        "Hello there, this is an automatic message", # Mensaje en el email
        "vladimir@unsa.com",                        # El correo que envia
        ["linoy54385@lukaat.com"],                  # los correos a los que
        fail_silently=False,
        )
    return render(request, 'send/index.html')