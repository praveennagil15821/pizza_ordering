from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your Account has been created!')
            return redirect('login')
        


    else:
        form = SignUpForm()
    heading="SignUp"
    content={
            'heading':heading,
            'form':form
        }   

    return render(request, 'user/signup.html',content)

