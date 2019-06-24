from django.shortcuts import render,redirect
from .forms import SignupForm
from .models import UserDetails,Gender
# Create your views here.


def index(request):

	return render(request, 'datacentre/index.html', {})


def add_data(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form .is_valid():
			instance = form.save(commit=False)
			if UserDetails.objects.filter(email=instance.email).exists():
				error=True
				return render(request, 'datacentre/add.html', {'error':error,'form':form})
			else:
				instance.save()
				success=True
				return render(request, 'datacentre/add.html', {'form': form,'success':success})
	else:
		form=SignupForm()
		return render(request, 'datacentre/add.html', {'form': form})

def view_data(request):
	male = Gender.objects.get(pk=1) #gets status name weekly goal
	female = Gender.objects.get(pk=2)
	men = UserDetails.objects.filter(gender=male)
	women = UserDetails.objects.filter(gender=female)
		

	

	context ={'male':male,'female':female,'men':men,'women':women,}
	return render(request, 'datacentre/list.html/', context)