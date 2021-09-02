from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .import forms
from django.contrib import messages
from django.conf import settings
from .models import Payment
# Create your views here.



def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            my_context = {'payment': payment,
                          'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY}
            return render(request, 'make_payment.html', my_context)
    else:
        payment_form = forms.PaymentForm()
        context2 = {'payment_form': payment_form}
    return render(request, 'payment/initiate_payment.html', context2)


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Verification Success")
    else:
        messages.error(request, "Verification Failed.")
    return redirect('initiate-payment')
