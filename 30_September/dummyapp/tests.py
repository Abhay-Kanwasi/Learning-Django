"""
In Django, the `python manage.py test` command is used to run tests for your django project. It is a management command that triggers the test runner provided by Django.

Django set up a test environment for running the tests. It creates a separate database, often referred to as the test database, to isolate the test data from your development database or production database. It also applies migrations to the test db to provide consistent starting point for the tests.

During the test execution, Django provides various assertion methods(e.g. assertEqual, assertTrue) that you can use to verify the expected behaviour of your code.
"""

from django.db import transaction, IntegrityError
from django.test import TestCase
from decimal import Decimal

from unicodedata import category

from .models import Services, Category, Pricing, Form


class ModelTests(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Category1', is_active=True)
        self.category2 = Category.objects.create(name="Category2", is_active=False)
        self.category3 = Category.objects.create(name="Category3", is_active=True)
        self.category4 = Category.objects.create(name="Category4", is_active=True)
        self.category5 = Category.objects.create(name="Category5", is_active=True)

        self.pricing1 = Pricing.objects.create(price=2.0, is_active=True)
        self.pricing2 = Pricing.objects.create(price=1.8, is_active=True)
        self.pricing3 = Pricing.objects.create(price=4.6, is_active=False)
        self.pricing4 = Pricing.objects.create(price=5.0, is_active=True)
        self.pricing5 = Pricing.objects.create(price=5.0, is_active=False)
        self.pricing6 = Pricing.objects.create(price=5.0, is_active=True)

        self.form1  = Form.objects.create(name='Form1', username='Form1User', password='Form1Password')
        self.form2 = Form.objects.create(name="Form2", username="Form2User", password="Form2Password")
        self.form3 = Form.objects.create(name="Form3", username="Form3User", password="Form3Password")
        self.form4 = Form.objects.create(name="Form4", username="Form4User", password="Form4Password")
        self.form5 = Form.objects.create(name="Form5", username="Form5User", password="Form5Password")

        self.service1 = Services.objects.create(name='Service1', description='Service1Description', is_active=True, pricing=self.pricing1)
        self.service2 = Services.objects.create(name="Service2", description="Service2", is_active=False,
                                                pricing=self.pricing2)
        self.service3 = Services.objects.create(name="Service3", description="Service3", is_active=False,
                                                pricing=self.pricing3)
        self.service4 = Services.objects.create(name="Service4", description="Service4", is_active=False,
                                                pricing=self.pricing4)
        self.service5 = Services.objects.create(name="Service5", description="Service5", is_active=False,
                                                pricing=self.pricing5)

    def test_case_to_add_form1_form2_to_service1(self):
        print("\nTesting addition of form1 and form2 into services")
        print(f'Initial value of form in service1: {self.service1.form.all()}')
        self.service1.form.add(self.form1, self.form2)
        print(f'After adding form1 and form2 in service1: {self.service1.form.all()}')
        self.assertTrue(self.service1.form.filter(name='Form1').exists())
        self.assertTrue(self.service1.form.filter(name='Form2').exists())
        self.assertEqual(1, self.service1.form.filter(name='Form1').count())
        self.assertEqual(1, self.service1.form.filter(name='Form2').count())
        print("Test passed!")

    def test_case_to_disassociate_form1_from_service1(self):
        print("\nTesting disassociation of form1 from service1")
        print(f'Initial value of form in service1: {self.service1.form.all()}')
        self.service1.form.add(self.form1, self.form2)
        print(f'Adding form1 and form2 in service1: {self.service1.form.all()}')
        self.service1.form.remove(self.form1)
        print(f'After removing form1 in service1: {self.service1.form.all()}')
        with self.assertRaises(Form.DoesNotExist):
            self.service1.form.get(name=self.form1.name)
        print("Test passed !")

    def test_case_for_create_form(self):
        print("\nTesting creation of form")
        form1_name = self.form1.name
        form1_username = self.form1.username
        form1_password = self.form1.password
        form = Form.objects.create(name=form1_name, username=form1_username, password=form1_password)
        print(f'Form created and values are: {form.__dict__}')
        self.assertEqual(form.name, form1_name)
        self.assertEqual(form1_username, form.username)
        self.assertEqual(form1_password, form.password)
        print("Test passed !")

    def test_case_for_update_form(self):
        print("\nTesting update of form")
        name = "New Name"
        username = "New UserName"
        password = "New Password"
        self.form1.name = name
        self.form1.username = username
        self.form1.password = password
        print(f'Form updated and values are: {self.form1.__dict__}')
        self.assertEqual(name, self.form1.name)
        self.assertEqual(username, self.form1.username)
        self.assertEqual(password, self.form1.password)
        print("Test passed !")

    def test_case_for_delete_form(self):
        print("\nTesting deletion of form")
        form_name = self.form1.name
        self.form1.delete()
        with self.assertRaises(Form.DoesNotExist):
            Form.objects.get(name=form_name)
        print("Test passed !")

    def test_case_for_create_price(self):
        print("\nTesting creation of price")
        print(Pricing.objects.all().values())
        price = self.pricing1.price
        is_active = self.pricing2.is_active
        pricing = Pricing.objects.create(price=price, is_active=is_active)
        self.assertEqual(price, pricing.price)
        print("Test passed !")

    def test_case_for_update_price(self):
        print("\nTesting price update")
        new_price = 21.8
        self.pricing1.price = new_price
        self.pricing1.save()
        self.assertEqual(self.pricing1.price, new_price)
        print("Test passed !")

    def test_case_for_delete_price(self):
        print("\nTesting price delete")
        self.pricing1.delete()
        with self.assertRaises(Pricing.DoesNotExist):
            Pricing.objects.get(price=self.pricing1.price)

    def test_unique_price_for_each_service(self):
        print("\nTesting unique price per service")
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                service = Services.objects.create(name='service', pricing=self.pricing1)
        print("Test passed !")

    def test_for_price_query_from_service(self):
        print("\nTesting price query")
        queried_service = Services.objects.get(pricing__price=2.0)
        self.assertEqual(queried_service, self.service1)
        print("Test passed !")

    def test_case_for_creating_category(self):
        print("\nTesting creation of category")
        name = self.category1.name
        is_active = self.category2.is_active
        Category.objects.create(name=name, is_active=is_active)
        self.assertTrue(Category.objects.filter(name=self.category1.name).exists())
        self.assertEqual(name, self.category1.name)
        self.assertEqual(is_active, self.category2.is_active)
        print("Test passed !")

    def test_case_for_creating_service(self):
        print("\nTesting creation of service")
        service = Services.objects.create(name='service', pricing=self.pricing6, description='description')
        service.form.add(self.form1)
        service.categories.add(self.category1)
        self.assertTrue(service.categories.filter(name="Category1").exists())
        print("Test passed !")

    def test_remove_category1_from_service1(self):
        print("\nTesting removing category from service1")
        self.service1.categories.add(self.category1)
        self.service1.categories.remove(self.category1)
        self.assertFalse(self.service1.categories.filter(name="Category1").exists())
        print("Test passed !")

