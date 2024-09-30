from django.shortcuts import render, redirect,get_object_or_404
from .models import Matumizi
from django.contrib import messages

# Create your views here.
def list(request):
	list = Matumizi.objects.order_by('-created_at')[:5]
	context = {'list':list}
	return render(request, 'matumizi.html', context)

def addMatumizi(request):
    if request.method == 'POST':  # Corrected to check 'POST' as a string
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        # Create a new entry in the database
        Matumizi.objects.create(title=title, price=price, description=description, status=status)
        
        messages.success(request, 'Expenses saved!')
        
        return redirect('list')  # Added 'return' to properly redirect

    return render(request, 'addMatumizi.html')

def deleteMatumizi(request, id):
	matumizi = get_object_or_404(Matumizi, id=id)
	matumizi.delete()
	messages.success(request, "Expense deleted!")

	return redirect('list')

def editMatumizi(request, id):
    # Get the Matumizi instance or return a 404 error if not found
    matumizi = get_object_or_404(Matumizi, id=id)
    
    if request.method == 'POST':
        # Get data from the POST request
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        status = request.POST.get('status')

        # Update the instance with new data
        matumizi.title = title
        matumizi.price = price
        matumizi.description = description
        matumizi.status = status
        matumizi.save()  # Save the updated instance
        
        messages.success(request, 'Expense updated successfully!')
        return redirect('list')  # Redirect to the list view after saving
    else:
        # Render the edit form with existing data for GET requests
        return render(request, 'editMatumizi.html', {'matumizi': matumizi})  # 

