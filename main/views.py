import json
import datetime
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST

from main.models import Product

# --- Page Rendering Views ---

@login_required(login_url='/login')
def show_main(request):
    """Render the main page shell. Data is loaded via AJAX."""
    context = {'last_login': request.COOKIES.get('last_login', 'Never')}
    return render(request, "main.html", context)

def register(request):
    """Render the registration page shell."""
    return render(request, 'register.html')

def login_user(request):
    """Render the login page shell."""
    return render(request, 'login.html')

def logout_user(request):
    """Handle user logout and redirect."""
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# --- AJAX API Views ---

@login_required(login_url='/login')
def get_products_json(request):
    """API endpoint to get products in JSON format, with filtering."""
    filter_type = request.GET.get("filter")
    products = Product.objects.filter(user=request.user) if filter_type == "my" else Product.objects.all()
    
    data = [{
        "id": str(product.id), "name": product.name, "brand": product.brand,
        "category": product.get_category_display(), "size": product.get_size_display(),
        "description": product.description, "price": product.price, "stock": product.stock,
        "thumbnail": product.thumbnail or "", "is_featured": product.is_featured,
        "user_id": product.user.id if product.user else None,
    } for product in products]
    
    return JsonResponse(data, safe=False)

@login_required(login_url='/login')
def get_product_for_detail_view_json(request, id):
    """API endpoint to get a single product's full details for viewing."""
    product = get_object_or_404(Product, pk=id)
    product.increment_views() 

    data = {
        "name": product.name, "brand": product.brand, "category": product.get_category_display(),
        "size": product.get_size_display(), "description": product.description, "price": product.price,
        "stock": product.stock, "thumbnail": product.thumbnail or "", "product_views": product.product_views,
        "user_username": product.user.username if product.user else "Anonymous", "is_featured": product.is_featured,
    }
    return JsonResponse(data)

@login_required(login_url='/login')
@require_POST
def add_product_ajax(request):
    """API endpoint to add a new product."""
    try:
        Product.objects.create(
            user=request.user, name=request.POST.get("name"), price=int(request.POST.get("price")),
            description=request.POST.get("description"), category=request.POST.get("category"),
            stock=int(request.POST.get("stock")), brand=request.POST.get("brand"),
            size=request.POST.get("size"), thumbnail=request.POST.get("thumbnail"),
            is_featured=request.POST.get("is_featured") == 'on'
        )
        return HttpResponse(b"CREATED", status=201)
    except (ValueError, TypeError) as e:
        return HttpResponseBadRequest(f"Invalid data: {e}")

@login_required(login_url='/login')
@require_POST
def delete_product_ajax(request, id):
    """API endpoint to delete a product."""
    try:
        product = get_object_or_404(Product, pk=id)
        if product.user == request.user:
            product.delete()
            return HttpResponse(b"DELETED", status=200)
        return HttpResponse(b"FORBIDDEN", status=403)
    except Product.DoesNotExist:
        return HttpResponse(b"NOT FOUND", status=404)

@login_required(login_url='/login')
def get_product_detail_json(request, id):
    """API endpoint to get a single product's details for editing."""
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return JsonResponse({"status": "forbidden"}, status=403)
    
    data = {
        "id": str(product.id), "name": product.name, "brand": product.brand, "category": product.category,
        "size": product.size, "description": product.description, "price": product.price,
        "stock": product.stock, "thumbnail": product.thumbnail or "", "is_featured": product.is_featured,
    }
    return JsonResponse(data)

@login_required(login_url='/login')
@require_POST
def edit_product_ajax(request, id):
    """API endpoint to update an existing product."""
    try:
        product = get_object_or_404(Product, pk=id)
        if product.user != request.user:
            return HttpResponse(b"FORBIDDEN", status=403)

        product.name = request.POST.get("name", product.name)
        product.price = int(request.POST.get("price", product.price))
        product.description = request.POST.get("description", product.description)
        product.category = request.POST.get("category", product.category)
        product.stock = int(request.POST.get("stock", product.stock))
        product.brand = request.POST.get("brand", product.brand)
        product.size = request.POST.get("size", product.size)
        product.thumbnail = request.POST.get("thumbnail", product.thumbnail)
        product.is_featured = request.POST.get("is_featured") == 'on'
        product.save()
        return HttpResponse(b"UPDATED", status=200)
    except (ValueError, TypeError):
        return HttpResponseBadRequest("Invalid data")

@require_POST
def register_ajax(request):
    """API endpoint for user registration."""
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": "success", "message": "Account created successfully!"}, status=201)
    errors = json.loads(form.errors.as_json())
    return JsonResponse({"status": "error", "errors": errors}, status=400)

@require_POST
def login_ajax(request):
    """API endpoint for user login."""
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse({"status": "success", "message": "Login successful!"})
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    return JsonResponse({"status": "error", "message": "Invalid username or password."}, status=400)