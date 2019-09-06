from django.shortcuts import render,redirect
from .models import Circular

# Create your views here.
def circular(request):
	circular_all=Circular.objects.all()
	return render(request,'circular_list.html',{'circulars':circular_all})

def create_circular(request):
	if request.method=="POST":
		date = request.POST['date']
		content = request.POST['content']
		signed = request.POST['is_signed']
		if signed=="on":
			is_signed=True
		else:
			is_signed=False

		posted_by=request.user

		circular = Circular(date=date,content=content,is_signed=is_signed,posted_by=posted_by)
		circular.save()

		return redirect('/circulars/')

	return render(request,'create_circular.html')
