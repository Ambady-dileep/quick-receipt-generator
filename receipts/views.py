from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum
from .models import Customer,Receipt,Item 
from .forms import ReceiptForm, ItemFormSet

# Create your views here.

def test_view(request):
    return JsonResponse({'message':"Hello from Django"})

def home_view(request):
    return HttpResponse("Welcome to the Quick Receipt Generator App!")

def customers_list(request):
    customers = Customer.objects.order_by('-created_at')
    context = {'customers':customers}
    return render(request,'receipts/customers_list.html',context)

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Customer.objects.create(name=name,email=email,phone=phone)
        return redirect('customers_list')
    return render(request,'receipts/add_customer.html')

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=405)

def add_or_edit_receipt(request, receipt_id=None):
    if receipt_id:
        receipt = get_object_or_404(Receipt, id=receipt_id)
        customer = receipt.customer
        title = "Edit Receipt"
    else:
        customer_id = request.GET.get('customer_id') or request.POST.get('customer_id')
        customer = get_object_or_404(Customer, id=customer_id)
        receipt = None
        title = "Add New Receipt"

    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt)
        formset = ItemFormSet(request.POST, instance=receipt)

        if form.is_valid() and formset.is_valid():
            new_receipt = form.save(commit=False)
            new_receipt.customer = customer

            # Save receipt without calculating total yet
            new_receipt.save()

            # Save the items first
            formset.instance = new_receipt
            formset.save()

            # ✅ Now calculate and update the total properly
            new_receipt.total = new_receipt.calculate_total()
            new_receipt.save()


            return redirect('customer_receipts', customer_id=customer.id)
    else:
        form = ReceiptForm(instance=receipt)
        formset = ItemFormSet(instance=receipt)

    return render(request, 'receipts/receipt_form.html', {
        'form': form,
        'formset': formset,
        'title': title,
        'is_edit': receipt_id is not None,
        'customer': customer
    })


def receipt_detail(request,receipt_id):
    receipt = get_object_or_404(Receipt,id=receipt_id)
    return render(request,'receipts/receipt_detail.html',{'receipt':receipt})

def customer_receipts(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    receipts = Receipt.objects.filter(customer=customer).order_by('-date_created')

    print("Customer:", customer)
    print("Receipts found:", receipts.count())
    for r in receipts:
        print(f"Receipt #{r.id}, Total: ₹{r.total}")

    grand_total = receipts.aggregate(total=Sum('total'))['total'] or 0

    return render(request, 'receipts/customer_receipts.html', {
        'customer': customer,
        'receipts': receipts,
        'grand_total': grand_total
    })
