from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from datetime import datetime

# Create your views here.
def index(request):   
    all_Prod = []
    category_names = Product.objects.values('category')
    categories = {item['category'] for item in category_names}
    for every_category in categories:
        prod = Product.objects.filter(category = every_category)
        n = len(prod)
        nSlides = n//4  + ceil((n/4) - (n//4))
        all_Prod.append([prod, range(1, nSlides), nSlides])
    params = {'all_prod' : all_Prod}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    param = {'action' : None}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact = Contact(name = name, email = email, phone = phone, query = query)
        contact.save()
        param =  {'action' : 'sent'}
    return render(request, 'shop/contact.html', param)

def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('orderId')
        email = request.POST.get('email')        
        try:
            order = Order.objects.filter(order_id = order_id, email = email)            
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id = order_id)
                updates = []
                for item in update:
                    updates.append({'text' : item.update_desc,  'time': item.timestamp.strftime("%m/%d/%Y, %H:%M:%S, %A")})
                    response = json.dumps([updates, order[0].items_json], default = str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.objects.filter(id = myid)
    param = {'product' : product[0]}
    return render(request, 'shop/prodView.html', param)

def checkout(request):
    param = {'action' : None}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        items_json = request.POST.get('items_json')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address1') + " " + request.POST.get('address2')
        city = request.POST.get('city')        
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')        
        order = Order(name=name, email=email,items_json=items_json, contact=contact_no, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        id = order.order_id
        order_update = OrderUpdate(order_id=id, update_desc="Your Order Has Been Placed")
        order_update.save()
        param =  {'action' : 'sent', 'id' : id}
    return render(request, 'shop/checkout.html',param)








    