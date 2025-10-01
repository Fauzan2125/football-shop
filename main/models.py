import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu Bola'),
        ('perlengkapan', 'Perlengkapan Latihan'),
        ('pakaian', 'Pakaian Kasual & Jaket'),
        ('aksesoris', 'Aksesoris'),
        ('memorabilia', 'Memorabilia'),
        ('lainnya', 'Lainnya'),
    ]

    SIZE_CHOICES = [
        # Ukuran Pakaian
        ('S', 'S - Small'),
        ('M', 'M - Medium'),
        ('L', 'L - Large'),
        ('XL', 'XL - Extra Large'),
        ('XXL', 'XXL - Double Extra Large'),
        # Ukuran Sepatu (Eropa)
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        # Untuk produk tanpa ukuran
        ('NA', 'N/A'),
    ]
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lainnya')
    thumbnail = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    size = models.CharField(
        max_length=5, 
        choices=SIZE_CHOICES, 
        default='NA',
        blank=True
    )
    rating = models.FloatField(default=0.0)
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save(update_fields=['product_views'])