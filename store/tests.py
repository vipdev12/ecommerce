from django.test import TestCase

# Create your tests here.


class TestHome(TestCase):
    def test_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class TestCart(TestCase):
    def test_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)


