from django.shortcuts import render
from django.http import *
from .models import *
from .forms import *
# Create your views here.

def index(request):
	cat=Categories.objects.all()
	template='product/home.html'
	content={
		'title':'All Products',
		'category':cat
	}
	return render(request, template, content)
	
def product_category(request,n):
    all_prod=Categories.objects.get(slug=n)
    categories=Categories.objects.all()
    return render(request,'product/product_category.html',{'category':all_prod,'categories':categories})

	
'''def detail1(request,d,slug):
    cart=Cart(request)
    #product=Product.objects.get(slug=slug)
    product = get_object_or_404(Product, id=d, slug=slug)
	if request.method=='POST':
		cartform=CartForm(request.POST)
		if cartform.is_valid():
			cd=cartform.cleaned_data
			cart.add(product=product,quantity=cd['quantity'],
			update_quantity=cd['update'])

			return redirect('cart:cart_detail')

    else:
        cartform=CartForm()
        
    return render(request,'product/detail.html',{'prod':product,'cartform':cartform})
'''
def detail(request, id):
	product=Product.objects.get(id=id)
	
	if request.method=='POST':
		form=NewCart(request.POST)
		if form.is_valid():
			f=form.save(commit=False)
			f.product=product
			f.save()
			return HttpResponseRedirect('/cartinfo/')
					
	else:
		form=NewCart()
		content={
			'title':'Product Form',
			'form':form,
			'product':product
			
		}
	return render(request,'product/detail_product.html', content)
		
def cart_detail(request):
	cart_record=Cart.objects.all()
	#print cart_record.product_price(3,4)
	d=[]
	
	for c in cart_record:
		d.append(c.product.price*c.quantity)
	
	
	content={
		'title':'Cart Detail',
		'cart_detail':cart_record,
		'total':sum(d)
	}
	return render(request, 'product/cart_detail.html', content)
	
def delete_product(request,id):
	product=Cart.objects.get(id=id)
	product.delete()
	return HttpResponseRedirect('/cartinfo/')
	