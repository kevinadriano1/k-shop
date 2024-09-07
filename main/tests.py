from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class ShowMainViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('main:show_main')

        # Create some test products
        self.product1 = Product.objects.create(
            name='barcelona 2024',
            price=100,
            description='this is great product with excellent features!',
            image_url='https://down-id.img.susercontent.com/file/id-11134207-7r98z-lsh0i1i3mid960'
        )
        self.product2 = Product.objects.create(
            name='manchester united 2024',
            price=200,
            description='this product is the best in the market!',
            image_url='https://footdealer.co/wp-content/uploads/2024/08/Maillot-de-face-Manchester-United-Domicile-2024-2025.jpg'
        )
        self.product3 = Product.objects.create(
            name='real madrid 2024',
            price=150,
            description='great product excellent features!',
            image_url='https://footdealer.co/wp-content/uploads/2023/06/Mailllot-Match-Real-Madrid-Domicile-2023-2024-1.jpg'
        )

    def test_show_main_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn('products', response.context)
        products = response.context['products']

        # Check if all products are in the context and match the expected dictionaries
        self.assertEqual(len(products), 3)
        self.assertEqual(products[0]['name'], 'barcelona 2024')
        self.assertEqual(products[1]['name'], 'manchester united 2024')
        self.assertEqual(products[2]['name'], 'real madrid 2024')

        # Check the content of the products
        self.assertContains(response, 'barcelona 2024')
        self.assertContains(response, 'manchester united 2024')
        self.assertContains(response, 'real madrid 2024')
