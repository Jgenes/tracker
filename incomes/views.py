from django.shortcuts import render, redirect,get_object_or_404
from .models import Income
from django.contrib import messages

# Create your views here.

def income(request):
	income = Income.objects.order_by('-created_at')
	context = {'income':income}

	return render(request, 'income.html',context)

def deleteIncome(request, id):
	income = get_object_or_404(Income, id=id)
	income.delete()
	messages.success(request, "Income deleted!")

	return redirect('income')


def editIncome(request, id):
    # Get the Income instance or return a 404 error if not found
    income = get_object_or_404(Income, id=id)
    
    if request.method == 'POST':
        # Get data from the POST request
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
       
        # Update the instance with new data
        income.title = title
        income.price = price
        income.description = description
        income.save()  # Save the updated instance
        
        messages.success(request, 'Income updated successfully!')
        return redirect('income')  # Redirect to the list view after saving
    else:
        # Render the edit form with existing data for GET requests
        return render(request, 'editIncome.html', {'income': income})  # Pass 'income' instead of 'matumizi'



def addIncome(request):
    if request.method == 'POST':  # Corrected to check 'POST' as a string
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        
        # Create a new entry in the database
        Income.objects.create(title=title, price=price, description=description)
        
        messages.success(request, 'Income saved!')
        
        return redirect('income')  # Added 'return' to properly redirect

    return render(request, 'addIncome.html')