from django.test import TestCase, Client
from .models import User, Crop

class AgriPortalTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.phone = '1234567890'
        self.name = 'TestUser'

    def test_user_registration_and_otp(self):
        response = self.client.post('/login/', {'phone': self.phone, 'name': self.name})
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(phone=self.phone)
        self.assertIsNotNone(user.otp)

    def test_otp_verification_success(self):
        user = User.objects.create(phone=self.phone, name=self.name, otp='123456')
        session = self.client.session
        session['phone'] = self.phone
        session.save()
        response = self.client.post('/verify/', {'otp': '123456'})
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertTrue(user.is_verified)

    def test_role_selection(self):
        user = User.objects.create(phone=self.phone, name=self.name, is_verified=True)
        session = self.client.session
        session['user_id'] = user.id
        session.save()
        response = self.client.post('/role/', {'role': 'buyer'})
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.role, 'buyer')

    def test_dashboard_as_farmer(self):
        user = User.objects.create(phone=self.phone, name=self.name, is_verified=True, role='farmer')
        session = self.client.session
        session['user_id'] = user.id
        session.save()
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_as_buyer(self):
        user = User.objects.create(phone=self.phone, name=self.name, is_verified=True, role='buyer')
        session = self.client.session
        session['user_id'] = user.id
        session.save()
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

