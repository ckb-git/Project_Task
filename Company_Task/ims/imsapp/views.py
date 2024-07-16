from django.shortcuts import render , redirect 

# Create your views here.
from imsapp.form import inventoryForm, ordersForm,transactionForm
from imsapp.models import Inventory, Orders,Transaction


def home(request):
    # # Calculate the required statistics
    # total_profit = sum(item.profit_earned for item in Inventory.objects.all())
    # total_items_in_stock = sum(item.quantity for item in Inventory.objects.all())
    # # Add more statistics calculations as needed
    # context = {
    #     'total_profit': total_profit,
    #     'total_items_in_stock': total_items_in_stock,
    #     # Add more statistics data to pass to the template
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')


def addnew(request):  
    if request.method == "POST":  
        form = inventoryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_inv')  
            except:  
                pass
    else:  
        form = inventoryForm()  
    return render(request,'add_inv.html',{'form':form}) 
# index
def show_inv(request):  
    inventory = Inventory.objects.all()  
    return render(request,'show_inv.html',{'inventory':inventory}) 

def edit(request, id):  
    inventory = Inventory.objects.get(id=id)  
    return render(request,'edit.html', {'inventory':inventory})  

def update(request, id):  
    inventory = Inventory.objects.get(id=id)  
    form = inventoryForm(request.POST, instance = inventory)  
    #print(form.is_valid())
    if form.is_valid():  
        form.save()  
        return redirect("/show_inv")  
    else:
        return render(request, 'edit.html', {'inventory': inventory})  
     
def destroy(request, id):  
    inventory = Inventory.objects.get(id=id)  
    inventory.delete()  
    return redirect("/show_inv")  

#cart
def cart(request,id): 
    inventory = Inventory.objects.get(id=id)   
    return render(request,'cart.html',{'inventory':inventory}) 



# def Orderlist(request):
#     list = Orders.objects.all()
#     l=list.values()
#     context={'l':l}
#     return render(request,'ord.html',context=context)


def ord(request,id):
    qs=Inventory.objects.get(id=id)
    
    initial_data={
        "name":qs.name,
        "item":qs.id,
        "quantity":1,
        "selling_price":qs.selling_price

    }
    # print(initial_data)
    if request.method=='POST':
        form = ordersForm(request.POST)
        # print(form.is_valid())
        # print(form)
        if form.is_valid():
            
            quantity=request.POST['quantity']
            qs.quantity=quantity
            qs.save()
            form.save()
            return redirect('/ord_table')
        else:
            form=ordersForm(instance=qs,initial=initial_data)
        context={'form':form,'qs':qs}
        return render(request,'cart.html',context)


    
    


    # item_id=request.GET.get('item_id')
    # item=Inventory.objects.get(id=item_id)
    # # Orders(item=item).save()
    # # return redirect('/ord_table')
    # form= ordersForm(request.POST,instance=item)
    # if request.method=='POST':
    #     # form = OrderForm(request.POST)
    #     form = ordersForm(request.POST,instance = item)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/ord_table')
    
    # return render(request,'cart.html',{'form':form,'inventory':item})
    
    
    
    # 


def ord_table(request):
    orders = Orders.objects.all()  
    return render(request,'ord.html',{'orders':orders}) 

def transaction(request):
    trans = Transaction.objects.all()  
    return render(request,'tra.html',{'trans':trans}) 


def ord_placed(request,id): 
    order = Orders.objects.get(id=id)   
    return render(request,'ord_placed.html',{'order':order}) 

def accept_reject(request,id):
    data=Orders.objects.get(id=id)
    
    initial_data={
        "name":data.name,
        "orid":data.id,
        "quantity":data.quantity,
        "selling_price":data.selling_price,
        "status":"success"

    }
    # print(initial_data)
    if request.method=='POST':
        form = transactionForm(request.POST)
        # print(form.is_valid())
        # print(form)
        if form.is_valid():
            status=request.POST['status']
            data.status=status
            data.save()
            form.save()
            data.delete()  
            return redirect('/transaction')
        else:
            form=ordersForm(instance=data,initial=initial_data)
        context={'form':form,'data':data}
        return render(request,'ord_placed.html',context)
    
# def reject(request, id):  
#     orders = Orders.objects.get(id=id)  
#     orders.delete()  
#     return redirect("/ord_table")

def ord_reject(request,id): 
    order = Orders.objects.get(id=id)   
    return render(request,'ord_reject.html',{'order':order}) 

        



