from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    
    context = {
        'app_name': "Moy's Football Store",  
        'npm': '2406344284',
        'name': 'Ahmad Fauzan Al Ayubi',      
        'class': 'PBP C',        
        'products': products,
    }
    
    return render(request, 'main.html', context)