from django.shortcuts import render, redirect
from .models import Payments



# Create your views here.

def payments_list(request):
	all_payments = Payments.objects.all()

	return render(request, "allpayments.html", {'payments': all_payments})

def create_payment(request):
    if request.method == 'POST':
    	name = request.POST['name']
    	branch =  request.POST['branch']
    	amount = request.POST['amount']
    	tog = request.POST['status']
    	if tog == 'paid':
    		status = True
    	else:
    		status = False
    	p = Payments(
    		name=name,
    		branch=branch,
    		amount=amount,
    		status=status
    		)
    	p.save()
    	return redirect('/pays/')
    return render(request, "create_payment.html")