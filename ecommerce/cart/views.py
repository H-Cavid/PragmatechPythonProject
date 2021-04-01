from django.shortcuts import render,redirect
from product.models import Product

def add_to_card(request,id):
    if request.method =="POST":
        if not request.session.get('card'):
            request.session['card']=list()
        else:
            request.session['card']=list(request.session['card'])#eger cart varsa sesiyada onu list formasina sal

        items=next((item for item in request.session['cart'] if item['id']==id),False)

        add_data={
            'id':id,
            'quantity':1,
        }

        if not items:
            request.session['card'].append(add_data)
            request.session.modifier=True
        return redirect('cards_products')

def cards_products(request):
    #product={'id': 6, 'quantity': 1} [{}]
    products = []
    total=0
    for product in request.session['card']:
        p_data=dict(product)
        id=p_data['id']
        quantity=p_data['quantity']
        obj=Product.objects.get(id=id)
        products.append((obj,quantity))
        if not obj.product_discount_price:
            total += obj.product_price * quantity
        else:
             total +=obj.product_discount_price * quantity
    
    context={
        "pro":products,
        "products_total":total
    }
    print(products)
    return render(request, 'cards_products.html',context)

