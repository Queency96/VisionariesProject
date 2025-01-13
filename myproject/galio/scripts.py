# scripts/setup_roles.py
from django.contrib.auth.models import Group, Permission

def setup_roles():
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    vendor_group, _ = Group.objects.get_or_create(name='Vendor')
    customer_group, _ = Group.objects.get_or_create(name='Customer')

    # Assign permissions (customize as needed)
    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)
