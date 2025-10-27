"""
DAO (Data Access Object)

Structural pattern that separates the business logic from data access logic.

It acts as a middle layer:
- Database/Models (Persistence layer)
- Service/Business Layer (Where code logic lives)

The main goal is to isolate the data-handling code -- so if your database, ORM or data source changes, your upper layer remain unaffected.

How DAO fits in Django Project
A Django project typically has:
- models.py : defines ORM models.
- views.py : handles HTTP requests/responses.
- services.py : handles service/business logic (optional).
- dao.py : handles direct database interactions (optional).

DAO sits between models and service.

Views -> Service Layer -> DAO Layer -> Model (DB)


Without DAO:
- Remove ORM | Code Repetition (file path) | More files to modify

Example: Your service or views might do things like:
         Employees.objects.filter(age__gt=25)
         Employees.objects.create(name='Abhay', salary=30)
    Here, data access logic mixed business logic.

With DAO:
- You create a DAO class responsible for all database operations related to Employees.

DAO Responsibilities:
- fetch_all_employees_data
- fetch_employees_by_id
- update_employee

Now you service layer will never directly call .objects.filter() or .create()

It will instead call:
    EmployeesDAO.get_all_employees()
    EmployeesDAO.create_employee()

If someday you switch from Django ORM to raw SQL or another data source, you only need to change the code inside DAO, not elsewhere.

FLOW: Views --> Service --> DAO --> Model ---> Database
"""

from .models import Services, Category, Pricing, Form

class ModelDAO:
    """
        This DAO is made for all the database operations
    """

    @staticmethod
    def get_all_services_with_active_prices():
        services_with_active_prices = Services.objects.filter(pricing__is_active=True)
        return services_with_active_prices

    @staticmethod
    def get_all_active_prices():
        active_prices = Pricing.objects.filter(is_active=True)
        return active_prices

    @staticmethod
    def get_enable_categories_with_atleast_one_active_service():
        enable_categories = Category.objects.filter(is_active=True).filter(services__is_active=True).distinct()
        return enable_categories

    @staticmethod
    def disassociate_category_from_service(category_object, service_object):
        service_object.categories.remove(category_object)
        return service_object

    @staticmethod
    def disassociate_form_from_services(form_object, service_object):
        service_object.forms.remove(form_object)
        return service_object

    @staticmethod
    def disassociate_form_from_service_by_name(service_name, form_name):
        service = Services.objects.get(name=service_name)
        form = Form.objects.get(name=form_name)
        service.form.remove(form)
        return service

    @staticmethod
    def disassociate_form_from_service_by_id(service_id, form_id):
        services = Services.objects.get(id=service_id)
        form = Form.objects.get(id=form_id)
        services.form.remove(form)
        return services

    @staticmethod
    def get_services_with_active_categories():
        services_with_active_categories = Services.objects.filter(categories__is_active=True).distinct()
        return services_with_active_categories

    @staticmethod
    def get_all_forms_along_with_the_number_of_services_associated():
        forms = Form.objects.all()
        form_data = {}
        for form in forms:
            form_data = {
                'name': form.name,
                'username': form.username,
                'password': form.password,
                'services count': form.services.count(),
            }
        return form_data

    @staticmethod
    def get_all_categories_along_with_the_numbers_of_services_associated():
        categories = Category.objects.all()
        form_data = {}
        for category in categories:
            form_data = {
                'name': category.name,
                'is_active': category.is_active,
                'services count': category.services.count(),
            }
        return form_data

    @staticmethod
    def get_all_services_along_with_the_number_of_categories_associated():
        services = Services.objects.all()
        form_data = {}
        for service in services:
            form_data = {
                'name' : service.name,
                'description' : service.description,
                'categories': service.categories.count(),
            }
        return form_data