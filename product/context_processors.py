from .models import *

#make a variable available in all templates
def cart(request):
	cart = Cart.objects.all()
	d=[]
	
	for i in cart:
		d.append(i.quantity)
	request.session['cart']=sum(d)
	#del request.session['cart']
	return {'cart': sum(d)}
