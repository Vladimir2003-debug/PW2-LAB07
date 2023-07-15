from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):
    email = request.POST['email']
    message = request.POST['message']
    print(message)
    print(email)
    """
    send_mail(
        "Hello from Vladimir Company",              # Asunto del email
        message,                                    # Mensaje en el email
        "vladimir@unsa.com",                        # El correo que envia
        [email],                                    # los correos a los que
        fail_silently=False,
        )
    """
    return render(request, 'send/index.html')

def index_view(request):
    return render(request, 'index.html',{})