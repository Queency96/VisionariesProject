# tests/test_roles.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings

# Modify ALLOWED_HOSTS to allow 'testserver' during testing
settings.ALLOWED_HOSTS.append('testserver')

class RoleBasedAccessTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.admin_user = self.User.objects.create_user(username='admin', role='admin', password='adminpass')
        self.vendor_user = self.User.objects.create_user(username='vendor', role='vendor', password='vendorpass')
        self.customer_user = self.User.objects.create_user(username='customer', role='customer', password='customerpass')

    def test_admin_access(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/adminDashboard/')
        self.assertEqual(response.status_code, 200)

    def test_vendor_access(self):
        self.client.login(username='vendor', password='vendorpass')
        response = self.client.get('/vendorDashboard/')
        self.assertEqual(response.status_code, 200)

    def test_customer_access(self):
        self.client.login(username='customer', password='customerpass')
        response = self.client.get('/customerDashboard')
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_redirect_for_vendor(self):
        self.client.login(username='vendor', password='vendorpass')
        response = self.client.get('/adminDashboard/')
        self.assertEqual(response.status_code, 302)  # Redirect since vendor shouldn't access admin dashboard

    def test_vendor_dashboard_redirect_for_admin(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/vendorDashboard/')
        self.assertEqual(response.status_code, 302)  # Redirect since admin shouldn't access vendor dashboard
