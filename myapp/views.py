from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def home(request):
    return render(request, 'myapp/home.html')


@csrf_exempt
def print_message(request):
    if request.method == "POST":
        try:
            call_command('print_message')
            messages.success(request, 'Success! check terminal')
        except Exception as e:
            print(e)
        return redirect('home')
    else:
        return redirect('home')
