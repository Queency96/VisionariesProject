from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model





# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'category')  # Ensures subcategories are unique within a category

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name





# Defining a custom user model that includes a role field for Admin, Vendor, and Customer.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    def is_admin(self):
        return self.role == 'admin'

    def is_vendor(self):
        return self.role == 'vendor'

    def is_customer(self):
        return self.role == 'customer'
    

class Meta:
    verbose_name = "User"               # Singular name for the model
    verbose_name_plural = "Users"      # Plural name for the model
    app_label = 'auth'                 # Ensures it appears under "Authentication and Authorization"





# Get the custom user model
User = get_user_model()

class OrderStatus(models.TextChoices):
    """
    Enum-like class for order status choices.
    """
    PENDING = 'Pending', 'Pending'
    PROCESSING = 'Processing', 'Processing'
    SHIPPED = 'Shipped', 'Shipped'
    DELIVERED = 'Delivered', 'Delivered'
    CANCELLED = 'Cancelled', 'Cancelled'

class Order(models.Model):
    """
    Represents a customer order.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Failed', 'Failed')],
        default='Pending'
    )
    shipping_address = models.TextField(null=True, blank=True)
    shipping_method = models.CharField(max_length=50, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        """
        Calculate the total order price, including tax.
        """
        subtotal = sum(item.total_price for item in self.items.all())
        self.total_price = subtotal + self.tax
        return self.total_price

    def save(self, *args, **kwargs):
        """
        Override save to ensure the total price is calculated before saving.
        """
        self.calculate_total()
        super().save(*args, **kwargs)

    def _str_(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    """
    Represents an item in an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """
        Override save to calculate total price and update product stock.
        """
        self.total_price = self.price_per_item * self.quantity

        # Update product stock if this is a new instance
        if not self.pk:
            if self.product.stock < self.quantity:
                raise ValueError(f"Insufficient stock for {self.product.name}")
            self.product.stock -= self.quantity
            self.product.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Override delete to restore product stock.
        """
        self.product.stock += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)

    def _str_(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"

class OrderStatusHistory(models.Model):
    """
    History of status changes for an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_history')
    previous_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Order #{self.order.id} status changed to {self.new_status}"
