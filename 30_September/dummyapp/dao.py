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
