from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category, SubCategory, Product

# Register CustomUser under Authentication and Authorization
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
  list_filter = ['role', 'is_staff', 'is_active']
  fieldsets = UserAdmin.fieldsets + (
      ('Role Information', {'fields': ('role',)}),
  )
  add_fieldsets = UserAdmin.add_fieldsets + (
      ('Role Information', {'fields': ('role',)}),
  )

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'description']

# SubCategory Admin
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'category', 'description']

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'price', 'stock', 'category', 'subcategory', 'is_available']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'description']

@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'category', 'description']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'price', 'stock', 'category', 'subcategory', 'is_available']
  
  