# userAuth/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from matumizi.models import Matumizi
from incomes.models import Income
from django.db.models import Sum


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Setting session
            request.session['username'] = user.username
            request.session['user_id'] = user.id  # Use user.id instead of user.user_id

            return redirect('dashboard')
        else:
            messages.error(request, "Unsuccessful login")
    return render(request, 'index.html')  #

def signUp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")  # Corrected from message.error to messages.error
            return redirect('signUp')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
            return redirect('signUp')

        # Create the user (fixed argument order)
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Set additional fields
        user.first_name = first_name
        user.last_name = last_name
        user.save()  # Save the user object with additional fields

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('index')
    
    return render(request, 'index.html')


@login_required
def dashboard(request):
    username = request.session.get('username', request.user.get_full_name() or request.user.username)
    user_id = request.session.get('user_id', None)

    # Calculate total expenses
    total_expenses_aggregate = Matumizi.objects.aggregate(total_expenses=Sum('price'))  # Use 'price' or correct field name
    total_expenses = total_expenses_aggregate['total_expenses'] if total_expenses_aggregate['total_expenses'] is not None else 0

    # Calculate total income
    total_income_aggregate = Income.objects.aggregate(total_income=Sum('price'))  # Use 'amount' or correct field name
    total_income = total_income_aggregate['total_income'] if total_income_aggregate['total_income'] is not None else 0

    return render(request, 'dashboard.html', {
        'username': username,
        'user_id': user_id,
        'total_expenses': total_expenses,
        'total_income': total_income
    })
# def expenses_summary(request):
#     total_expenses = Matumizi.objects.aggregrate(price=Sum('price'))
#     return render(request, 'dashboard.html', {'total_expenses': total_expenses})


