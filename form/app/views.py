import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Crop, Request
from django.contrib import messages

# Simulated OTP sending (print to console)
def send_otp(phone, otp):
    print(f"Sending OTP to {phone}: {otp}")

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        name = request.POST.get('name', '')
        user, created = User.objects.get_or_create(phone=phone, defaults={'name': name})
        otp = str(random.randint(100000, 999999))
        user.otp = otp
        user.save()
        send_otp(phone, otp)
        request.session['phone'] = phone
        return redirect('verify_otp')
    return render(request, 'core/login.html')

def verify_otp(request):
    if request.method == 'POST':
        otp_input = request.POST['otp']
        phone = request.session.get('phone')
        user = User.objects.filter(phone=phone).first()
        if user and user.otp == otp_input:
            user.is_verified = True
            user.save()
            request.session['user_id'] = user.id
            if not user.role:
                return redirect('select_role')
            return redirect('dashboard')
