from django.shortcuts import render
from django.core.mail import send_mail 

# Create your views here.
def index(request):
    return render(request, 'index.html')
def payment(request):
    if request.method == "GET":
        amount = request.GET.get('amount')
        email = request.GET.get('email')
        Email = request.GET.get('Email')
        print(email,Email)
        content = f"Payment recieved of {amount}"
        send_mail("Payment Gateaway Integration", content, "paymentsp07@gmail.com", [email])
        context = {
            "amount": amount,
        }
    return render(request, 'payment.html',context)