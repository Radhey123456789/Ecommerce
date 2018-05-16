from django import template

register = template.Library()


@register.filter(name='cart_len')
def cart_length(value):
    c=value.__len__()
    print 'hello'
    print c
    return c

@register.filter(name='cart_price')
def cart_price(value):
	#print 
    #c=value.product_price(value.quantity)
    #print 'hello'
    #print value
    return value.quantity*value.product.price