from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.forms import ModelForm
from food.models import Blog

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('server_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class ServerForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['restaurant','address','locations','landmark','zipcode','restaurantphn'
		,'restaurantemail','restaurantweb','features', 'openingstatus', 'timing',
		'From','To','facebookpage','twitterhandle','otherdetails']
		

def server_list(request, template_name='server_list.html'):
    food = Blog.objects.all()
    data = {}
    data['object_list'] = food
    return render(request, template_name, data)
	
def server_list1(request, template_name='login.html'):
    food = Blog.objects.all()
    data = {}
    data['object_list'] = food
    return render(request, template_name, data)	
	
	  
def pfbusi(request):
    
	
      return render(request, 'Addrest.html')	  
	  
def rest(request, template_name='rest.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})	  